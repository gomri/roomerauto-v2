from Vars import *
import re
from datetime import datetime

def get_date():
	todays_date = str(datetime.today().day)
	date_3_day_from_now = str(datetime.today().day + 3)
	if date_3_day_from_now >= '28':
		return todays_date
	else:
		return date_3_day_from_now

def get_supplier_type(url, regex):
	try:
		string_supplier_type = re.search(regex, url).group(2)
		if string_supplier_type == 'T':
			return 'T'
		elif string_supplier_type == 'E':
			return 'E'
		elif string_supplier_type == 'H':
			return 'H'
	except AttributeError:
		return 'P2P'


def print_test_report(source,
						test_case,
						cancellation_policy,
						supplier_type,
						tested):
	print ''
	print 'soure: ' + source
	print 'test_case: ' + test_case
	print 'cancellation_policy: ' + cancellation_policy
	print 'supplier_type: ' + supplier_type
	print 'tested: ' + str(tested)

def insert_data_to_dict(source,
						test_case,
						cancellation_policy,
						supplier_type,
						tested,
						dict_to_add_data_to):
	dict_to_add_data_to['source'].format(source=source)
	dict_to_add_data_to['test_case'].format(test_case=test_case)
	dict_to_add_data_to['supplier_type'].format(supplier_type=supplier_type)
	dict_to_add_data_to['cancellation_policy'].format(cancellation_policy=cancellation_policy)
	dict_to_add_data_to['tested'] = tested
	