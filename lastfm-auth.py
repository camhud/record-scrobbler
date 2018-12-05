# Authenticates user to last.fm to allow scrobbling

from urllib import parse
import webbrowser

# program-specific key and secret for initial request
api_key	= '8ca998e17cabfe7ee04d724e017830a9'
secret = 'b18306611432557eadca3d8b372ce74e'

# important urls
callback_url = "http://nickknudsen.photography/recordscrobbler/authorization"
api_url = 'http://ws.audioscrobbler.com/2.0/'
auth_url = 'http://www.last.fm/api/auth/?api_key'

# a unique identifier for this application, handed to discogs
user_agent = "record_scrobbler_test-0.1"

# send to auth endpoint to begin
webbrowser.open(auth_url + api_key + '&cb=' + callback_url)

# for testing purposes only
current_url = (input("Paste the redirect url here:\n")

# parse the redirect url for auth token
auth_token = parse.urlparse(current_url)[4]