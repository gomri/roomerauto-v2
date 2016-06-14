from Vars import *
	

def get_supplier_type(url, regex):
	string_supplier_type = re.search(regex, url).group(2)
	if string_supplier_type == 'T':
		return 'T'
	elif string_supplier_type == 'E':
		return 'E'
	elif string_supplier_type == 'H':
		return 'H'
	elif string_supplier_type == None:
		return 'P2P'

url = 'http://roomer-qa-1.herokuapp.com/hotels/quebec-hotels/hilton-quebec.h5438/44586420?rate_plan_id=2&rate_plan_token=e2c82945b4ede3fc7f0b2c4739adf1f8&orig_price=95&'

print get_supplier_type(url,REGEX['find_supplier_type'])