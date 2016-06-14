from Vars import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from error_handleing import *

def click_FC(driver,url=None):
	driver.find_element_by_css_selector(ENTRY_PAGE['book_button_FC']).click()

def open_secret_deal(driver,url=None):
	driver.find_element_by_css_selector(ENTRY_PAGE['unlock_secret_deal']['click_to_input_email']).click()
	error_handler(driver,'test')
	driver.find_element_by_id(ENTRY_PAGE['unlock_secret_deal']['fill_in_box']).send_keys(ENTRY_PAGE['unlock_secret_deal']['data_to_fill'])
	driver.find_element_by_name(ENTRY_PAGE['unlock_secret_deal']['click_unlock']).click()