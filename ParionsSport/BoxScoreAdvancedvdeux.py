from EndPointGetter import EndPointGetter
from DBQuery import DBQuery


class BoxScoreAdvancedvdeux(EndPointGetter, DBQuery):

    def __init__(self, GameID, i, j):
        self._endpoint = "boxscoreadvancedv2"
        self._params = {
            "GameID": GameID,
            "StartPeriod":i,
            "EndPeriod":j,
            "StartRange":1,
            "EndRange":1,
            "RangeType":1
        }

    def getQuarterInfosFromAPI(self):
        results = self._request()
        players = self._api_scrape(0)
        teams = self._api_scrape(1)
        return (players, teams);
