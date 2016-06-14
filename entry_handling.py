from Vars import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from error_handleing import *
from global_function import *
import re 


def click_FC(driver,url=None):
	page_url = USEFULL_COMMANDS['get_url']
	driver.find_element_by_css_selector(ENTRY_PAGE['book_button_FC']).click()
	return 'FC'

def click_NR(driver,url=None):
	driver.find_element_by_css_selector(ENTRY_PAGE['click_NR']).click()
	

	driver.find_element_by_css_selector(ENTRY_PAGE['click_book']).click()
	return 'NR'

def click_LH(driver,url=None):
	driver.find_element_by_css_selector('click_LH').click()
	driver.find_element_by_css_selector('click_book').click()
	return 'LH'
