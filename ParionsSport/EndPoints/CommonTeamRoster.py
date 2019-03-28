from EndPoints.EndPointGetter import EndPointGetter


class CommonTeamRoster(EndPointGetter):

    def __init__(self, teamID, SeasonID):
        self._endpoint = "commonteamroster"
        self._params = {
            "TeamID":teamID,
            "Season":SeasonID
        }

    def getRosterInfosFromAPI(self):
        results = self._request()
        teams = self._api_scrape(0)
        return teams;