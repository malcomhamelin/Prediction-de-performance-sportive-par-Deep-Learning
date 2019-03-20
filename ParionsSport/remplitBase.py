from DBQuery import DBQuery
from TeamInfoCommon import TeamInfoCommon
from CommonTeamRoster import CommonTeamRoster
from TeamGameLog import  TeamGameLog
from BoxScoreTraditionalvdeux import BoxScoreTraditionalvdeux
from BoxScoreSummaryvdeux import BoxScoreSummaryvdeux
from BoxScoreAdvancedvdeux import BoxScoreAdvancedvdeux



db = DBQuery()

idFirstTeam = 1610612737
idLastTeam = 1610612766

for i in range(idFirstTeam, idLastTeam+1):
    print("Insertion team n° : ")
    print(i)
    teamInfos = TeamInfoCommon(i)
    tabTeamInfos = teamInfos.getTeamInfosFromAPI()[0]
    db.insert_equipe_nba(tabTeamInfos)

    # TEAM ROOSTER
    Roster = CommonTeamRoster(i, "2018-19")
    Roster = Roster.getRosterInfosFromAPI()
    for joueur in Roster:
        print("Insertion joueur : ")
        print(joueur["PLAYER"])
        db.insert_joueur_nba(joueur)

for i in range(idFirstTeam, idLastTeam+1):
    # GAME LOG
    teamGLog = TeamGameLog(i, "2018-19")
    tabGames = teamGLog.getTeamGamesFromAPI()
    gamesAdded = list()

    for game in tabGames:
        if game in gamesAdded:
            print("Match déjà présent")
            continue

        print('insertion match : ')
        print(game)
        matchInfos = BoxScoreSummaryvdeux(game)
        (tabInfoGeneral, tabInfoLineScore) = matchInfos.getScoreSummaryInfoFromAPI()
        db.insert_match_nba(tabInfoGeneral, tabInfoLineScore)
        gamesAdded.append(game)

    for game in tabGames:
        print('insertion stats match : ')
        print(game)
        box = BoxScoreTraditionalvdeux(game,1,11)
        tab = box.getRosterInfosFromAPI()

        if i == tab[0]['TEAM_ID']:
            print("minutes : ")
            print(tab[0]['MIN'])
            db.insert_stats_equipe_match_nba(tab[0])
        else:
            print("minutes : ")
            print(tab[0]['MIN'])
            db.insert_stats_equipe_match_nba(tab[1])

        for j in range(1,11):

            statsAdvQt = BoxScoreAdvancedvdeux(game, j)
            statsTrdQt = BoxScoreTraditionalvdeux(game, j,j)

            for joueur in Roster:
                print("Insertion stats joueur quart-temps: ")
                db.insert_quart_temps_nba(statsTrdQt,statsAdvQt)

