from EndPointGetter import EndPointGetter
from DBQuery import DBQuery


class BoxScoreAdvancedvdeux(EndPointGetter, DBQuery):

    def __init__(self, GameID,i):
        self._endpoint = "boxscoreadvancedv2"
        self._params = {
            "GameID": GameID,
            "StartPeriod":i,
            "EndPeriod":i,
            "StartRange":1,
            "EndRange":1,
            "RangeType":1
        }

    def getQuarterInfosFromAPI(self):
        results = self._request()
        teams = self._api_scrape(0)
        return teams;
