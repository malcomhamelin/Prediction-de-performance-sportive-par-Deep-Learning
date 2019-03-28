from DBQueries.DBQuery import DBQuery
from EndPoints.TeamInfoCommon import TeamInfoCommon
from EndPoints.CommonTeamRoster import CommonTeamRoster
from EndPoints.TeamGameLog import  TeamGameLog
from EndPoints.BoxScoreTraditionalvdeux import BoxScoreTraditionalvdeux
from EndPoints.BoxScoreSummaryvdeux import BoxScoreSummaryvdeux
from EndPoints.BoxScoreAdvancedvdeux import BoxScoreAdvancedvdeux



db = DBQuery()

majTeamsPlayers = True

idFirstTeam = 1610612737
idLastTeam = 1610612766

if majTeamsPlayers:
    for i in range(idFirstTeam, idLastTeam+1):
        # Insertion des équipes
        print("Insertion team n° : ")
        print(i)
        teamInfos = TeamInfoCommon(i)
        tabTeamInfos = teamInfos.getTeamInfosFromAPI()[0]
        db.insert_equipe_nba(tabTeamInfos)

        # Insertion des joueurs
        Roster = CommonTeamRoster(i, "2017-18")
        Roster = Roster.getRosterInfosFromAPI()
        for joueur in Roster:
            print("Insertion joueur : ")
            print(joueur["PLAYER"])
            db.insert_joueur_nba(joueur)

for i in range(idFirstTeam, idLastTeam+1):
    # Recuparation des matchs de chaque equipe
    teamGLog = TeamGameLog(i, "2017-18")
    tabGames = teamGLog.getTeamGamesFromAPI()
    gamesAdded = list()

    for game in tabGames:
        # Insertion des matchs de chaque équipe
        if len(db.select_match(game)) == 0:
            print('insertion match : ')
            print(game)
            matchInfos = BoxScoreSummaryvdeux(game)
            (tabInfoGeneral, tabInfoLineScore) = matchInfos.getScoreSummaryInfoFromAPI()
            db.insert_match_nba(tabInfoGeneral, tabInfoLineScore)

    for game in tabGames:
        # Insertion des stats des matchs de chaque équipe
        print('insertion stats match : ')
        print(game)
        boxTraditionnal = BoxScoreTraditionalvdeux(game, 1, 11)
        statsTraditionnalPlayers, statsTraditionnalTeam = boxTraditionnal.getRosterInfosFromAPI()

        if i == statsTraditionnalTeam[0]['TEAM_ID']:
            db.insert_stats_equipe_match_nba(statsTraditionnalTeam[0])
        else:
            db.insert_stats_equipe_match_nba(statsTraditionnalTeam[1])

        # Insertion des statistiques pour chaque quart temps de chaque joueur
        if len(db.select_stats_match(game)) == 0:
            for j in range(1, 11):
                boxAdvancedQT = BoxScoreAdvancedvdeux(game, j, j)
                boxTraditionnalQT = BoxScoreTraditionalvdeux(game, j, j)
                statsAdvancedPlayersQT, statsAdvancedTeamsQT = boxAdvancedQT.getQuarterInfosFromAPI()
                statsTraditionnalPlayersQT, statsTraditionnalTeamsQT = boxTraditionnalQT.getRosterInfosFromAPI()

                for noJoueur in range(0, len(statsTraditionnalPlayersQT)):
                    print("Insertion qt n°", j, " joueur n°", noJoueur, " match n°", game)
                    db.insert_quart_temps_nba(j, statsTraditionnalPlayersQT[noJoueur],
                                              statsAdvancedPlayersQT[noJoueur])
