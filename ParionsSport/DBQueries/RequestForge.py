from fake_useragent import UserAgent
from requests import get


class RequestForgery:
	already_init = 0
	
	def __init__(self):
		if (RequestForgery.already_init == 0):
			ua = UserAgent()
			RequestForgery.user_agent = ua.random
			print(RequestForgery.user_agent)
			RequestForgery.already_init = 1
			#'user-agent': (u'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36'),  # noqa: E501
		self._base_url = 'http://stats.nba.com/stats/{endpoint}'
		self._headers = {
		    'user-agent': RequestForgery.user_agent, #('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'),
		    'Dnt': ('1'),
		    'Accept-Encoding': ('gzip, deflate, sdch'),
		    'Accept-Language': ('en'),
		    'origin': ('http://stats.nba.com')
		}
		self._cpt_errors = 0

	def get_json(self, endpoint, params):
		"""
		 Internal method to streamline our requests / json getting
		 Args:
		 endpoint (str): endpoint to be called from the API
		 params (dict): parameters to be passed to the API
		 Raises:
		 HTTPError: if requests hits a status code != 200
		 Returns:
		 json (json): json object for selected API call
		"""

		h = dict(self._headers)
		h['referer'] = 'https://stats.nba.com/stats/{endpoint}'
		_get = get(self._base_url.format(endpoint=endpoint), params=params,
		headers=h)
		# print _get.url
		_get.raise_for_status()
		return _get.json()
