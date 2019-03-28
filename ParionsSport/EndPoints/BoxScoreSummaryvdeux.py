from EndPoints.EndPointGetter import EndPointGetter
from DBQueries.DBQuery import DBQuery


class BoxScoreSummaryvdeux(EndPointGetter, DBQuery):

    def __init__(self, GameID):
        self._endpoint = "boxscoresummaryv2"
        self._params = {
            "GameID": GameID
        }

    def getScoreSummaryInfoFromAPI(self):
        result = self._request()
        tabInfoGeneral = self._api_scrape(0)
        tabInfoLineScore = self._api_scrape(5)
        return (tabInfoGeneral, tabInfoLineScore)
