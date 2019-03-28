from EndPoints.EndPointGetter import EndPointGetter


class TeamInfoCommon(EndPointGetter):

    def __init__(self, teamID):
        self._endpoint = "teaminfocommon"
        self._params = {
            "LeagueID": "00",
            "TeamID":teamID,
            "SeasonType":"Regular Season",
            "Season":"2018-19"
        }

    def getTeamInfosFromAPI(self):
        results = self._request()
        teams = self._api_scrape(0)
        return teams;