from EndPoints.EndPointGetter import EndPointGetter


class BoxScoreTraditionalvdeux(EndPointGetter):

    def __init__(self, GameID,i,j):
        self._endpoint = "boxscoretraditionalv2"
        self._params = {
            "GameID":GameID,
            "StartPeriod":i,
            "EndPeriod":j,
            "StartRange":1,
            "EndRange":1,
            "RangeType":1
        }

    def getRosterInfosFromAPI(self):
        results = self._request()
        players = self._api_scrape(0)
        teams = self._api_scrape(1)
        return (players, teams);
