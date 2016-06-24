import requests
import json
import re 
from Vars import *
from global_functions import *
import time

start_time = time.time()

header = {
    API['request_headers']['authorization']['key']: API['request_headers']['authorization']['value'].format(
    																token=API['email-token_pars']['kayak']['token_one']
    																),
    API['request_headers']['partner']['key']: API['request_headers']['partner']['value'].format(
    																email=API['email-token_pars']['kayak']['email']
    																),
    API['request_headers']['api-version']['key']: API['request_headers']['api-version']['value']
}

url = API['url'].format(
		env='qa-2',
		hotel_id=API['hotel_id'],
		check_in=API['check_in'],
		check_out=API['check_out']
	)
	

r = requests.get(url, None, headers=header)
content = r.content
x = json.loads(content)
for i in range(len(x)):
	room_url = x[i]['reservation']['url']
	get_source(REGEX['find_source'], room_url)
	get_redirect_url(REGEX['find_meta_redirect'], room_url, ROOMER['url'].format(env='qa-2')
																								)


print("--- %s seconds ---" % (time.time() - start_time))