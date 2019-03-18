from DBQuery import DBQuery
from TeamInfoCommon import TeamInfoCommon
from CommonTeamRoster import CommonTeamRoster
from TeamGameLog import  TeamGameLog
from BoxScoreTraditionalvdeux import BoxScoreTraditionalvdeux
from BoxScoreSummaryvdeux import BoxScoreSummaryvdeux

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
    Roster = CommonTeamRoster(i,"2018-19")
    Roster = Roster.getRosterInfosFromAPI()
    for joueur in Roster:
        print("Insertion joueur : ")
        print(joueur["PLAYER"])
        db.insert_joueur_nba(joueur)

    # GAME LOG
    teamGLog = TeamGameLog(i, "2018-19")
    tabGames = teamGLog.getTeamGamesFromAPI()



    for game in tabGames:
        print('insertion match : ')
        print(game)
        matchInfos = BoxScoreSummaryvdeux(game)
        (tabInfoGeneral, tabInfoLineScore) = matchInfos.getScoreSummaryInfoFromAPI()
        db.insert_match_nba(tabInfoGeneral, tabInfoLineScore)

    for game in tabGames:
        print('insertion stats match : ')
        print(game)
        box = BoxScoreTraditionalvdeux(game)
        tab = box.getRosterInfosFromAPI()[0]
        db.insert_stats_equipe_match_nba(tab)