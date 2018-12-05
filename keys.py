# this file is a temporary solution for storing important keys for the scrobbler

class discogsKeys:
	def __init__(self, token=None, secret=None):
		self._user_agent = "record_scrobbler_test-0.1"
		self._consumer_key = "JumzrdFQUamqVRRPICXr"
		self._consumer_secret = "jeOddrXBlFjJWmVwBIuMPQQQiELrcgFz"
		self._access_token = token
		self._access_secret = secret

class lastFMKeys:
	def __init__(self, key=None, secret=None):
		self._user_agent = 'Record Scrobbler'
		self._app_key = '8ca998e17cabfe7ee04d724e017830a9'
		self._app_secret = 'b18306611432557eadca3d8b372ce74e'
		self._key = key
		self._secret = secret

