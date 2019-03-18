from DBQuery import DBQuery
from TeamInfoCommon import TeamInfoCommon

db = DBQuery()

idFirstTeam = 1610612737
idLastTeam = 1610612766

for i in range(idFirstTeam, idLastTeam+1):
    print("Insertion team n° : ")
    print(i)
    teamInfos = TeamInfoCommon(i)
    tabTeamInfos = teamInfos.getTeamInfosFromAPI()[0]
    db.insert_equipe_nba(tabTeamInfos)
