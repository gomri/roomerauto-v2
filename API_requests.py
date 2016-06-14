import requests
import json
import re 
from Vars import *

hotel_id= range(100)

header = {
    "Authorization": "Token token=cd7de248487ac667fe3a6f60235ed1d0",
    "Partner": "eric@kayak.com",
    "API-Version": "1"
}
url = API['base'].format(
		env='qa-2',
		hotel_id=hotel_id,
		
	)

r = requests.get(url, None, headers=header)
content = r.content
x = json.loads(content)
print x 