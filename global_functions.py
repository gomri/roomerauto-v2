from Vars import *
import re
import datetime


def get_date(addDays=3):

    timeNow = datetime.datetime.now()
    if (addDays!=0):
        anotherTime = timeNow + datetime.timedelta(days=addDays)
    else:
        anotherTime = timeNow

    return anotherTime.day


def get_check_in(dateFormat="%Y-%m-%d"):

    timeNow = datetime.datetime.now()
    return timeNow.strftime(dateFormat)


def get_check_out(dateFormat="%Y-%m-%d", addDays=3):

    timeNow = datetime.datetime.now()
    if (addDays!=0):
        anotherTime = timeNow + datetime.timedelta(days=addDays)
    else:
        anotherTime = timeNow

    return anotherTime.strftime(dateFormat)

def get_hotel_id():
	list1 = range(100)
	list1 = str(list1).replace('[','').replace(']','')
	return list1


def get_supplier_type(regex, url):
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

def get_source(regex, url):
	reservation_source = re.search(regex, url).group(2)
	return reservation_source


def get_redirect_url(regex, url ,roomer_url):
	meta_redirect = re.search(regex, url).group(1)
	resevation_url = roomer_url + meta_redirect 
	return resevation_url	


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
	