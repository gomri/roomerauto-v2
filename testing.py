import requests
import json
import re 
import time
from API_requests import *
from Vars import *
from global_functions import *


class API_request(object):
	"""docstring for ClassName"""
	def __init__(self, header=None, url=None):
		self.header = header
		self.url = url

	def Connect_to_api(self):
		try:
		    response = requests.get(url, params=None, headers=header)
		except requests.exceptions.Timeout:
			response = requests.get(url, params=None,headers=header)
		    # Maybe set up for a retry, or continue in a retry loop
		except requests.exceptions.TooManyRedirects:
		    print 'URL was bad try a different one'
		except requests.exceptions.RequestException as e:
		    # catastrophic error. bail.
		    print e
		    sys.exit(1)
		if response.status_code != 200:
			response = response.status_code
		return response

	def get_rooms_url(self, response_content):
		_json_response_content = json.loads(response_content)
		for i in range(len(_json_response_content)):
			room_mate_redirect = _json_response_content[i]['reservation']['url']
			source = get_source(REGEX['find_source'], room_mate_redirect)
			reservation_url = get_redirect_url(REGEX['find_meta_redirect'], room_mate_redirect, ROOMER['url'].format(env='qa-2'))
		return source, reservation_url

kayak_rooms = API_request(url, header)
response_status = kayak_rooms.Connect_to_api().status_code
response_content = kayak_rooms.Connect_to_api().content
if response_status == 200:
	print kayak_rooms.get_rooms_url(response_content)






