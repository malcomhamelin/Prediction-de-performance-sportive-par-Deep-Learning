from EndPointGetter import EndPointGetter
from DBQuery import DBQuery


class TeamGameLog(EndPointGetter, DBQuery):

    def __init__(self, teamID, season ):
        self._endpoint = "teamgamelog"
        self._params = {
            "TeamID": teamID,
            "Season": season,
            "SeasonType": "Regular Season"
        }

    def getTeamGamesFromAPI(self):
        self._request()
        results = self._api_scrape(0)
        games = [result["Game_ID"] for result in results]
        return games
