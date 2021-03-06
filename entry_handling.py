from Vars import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from error_handling import *
from global_functions import *
import re 


def click_FC(driver,url=None):
	page_url = str(driver.current_url)
	supplier = get_supplier_type(REGEX['find_supplier_type'],
															page_url)	
	rate_plan = get_rate_plan(REGEX['find_rate_plan'],
															driver.current_url)
	driver.find_element_by_css_selector(ENTRY_PAGE['click_FC']).click()
	return 'FC', supplier, rate_plan

def click_NR(driver,url=None):
	driver.find_element_by_css_selector(ENTRY_PAGE['click_NR']).click()
	page_url = str(driver.current_url)
	supplier = get_supplier_type(REGEX['find_supplier_type'],
															driver.current_url)
	rate_plan = get_rate_plan(REGEX['find_rate_plan'],
															driver.current_url)
	driver.find_element_by_css_selector(ENTRY_PAGE['click_book']).click()
	return 'NR', supplier, rate_plan

def click_LH(driver,url=None):
	driver.find_element_by_css_selector(ENTRY_PAGE['click_LH']).click()
	page_url = str(driver.current_url)
	supplier = get_supplier_type(REGEX['find_supplier_type'],
															page_url)
	rate_plan = get_rate_plan(REGEX['find_rate_plan'],
															driver.current_url)
	driver.find_element_by_css_selector(ENTRY_PAGE['click_book']).click()
	return 'LH', supplier, rate_plan
