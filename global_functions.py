from Vars import *
import re

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
	print 'soure: ' + soure
	print 'test_case: ' + test_case
	print 'cancellation_policy: ' + cancellation_policy
	print 'supplier_type: ' + supplier_type
	print 'tested: ' + tested