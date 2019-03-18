"""
	Classe mere de toutes les classes EndPoints
"""
import time
from RequestForge import RequestForgery

class EndPointGetter:
	def _request(self):
		time.sleep(.40)
		req = RequestForgery()
		self._resultGet = req.get_json(self._endpoint, self._params)

	def _api_scrape( self, ndx ):
		try:
			headers = self._resultGet['resultSets'][ndx]['headers']
			values = self._resultGet['resultSets'][ndx]['rowSet']
		except KeyError:
			# This is so ugly but this is what you get when your data comes out
			# in not a standard format
			try:
				headers = self._resultGet['resultSet'][ndx]['headers']
				values = self._resultGet['resultSet'][ndx]['rowSet']
			except KeyError:
				# Added for results that only include one set (ex. LeagueLeaders)
				headers = self._resultGet['resultSet']['headers']
				values = self._resultGet['resultSet']['rowSet']
		return [dict(zip(headers, value)) for value in values]