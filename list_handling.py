from Vars import LIST_PAGE
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from Vars import RANDOM

def unlock_SD(driver):
	try:
		driver.find_element_by_css_selector(LIST_PAGE['unlock_secret_deal']['parent_element']).find_element_by_css_selector(LIST_PAGE['unlock_secret_deal']['select_input_field']).send_keys(LIST_PAGE['unlock_secret_deal']['data_to_fill'])
		driver.find_element_by_name(LIST_PAGE['unlock_secret_deal']['click_unlock']).click()
	except NoSuchElementException:
		pass

def click_random_room(driver,url=None):
	try:
		driver.find_elements_by_css_selector(LIST_PAGE['click_room_non_sd'])[RANDOM['rand_num']].click()
	except NoSuchElementException:
		driver.refresh()
		driver.find_element_by_css_selector(LIST_PAGE['click_room_non_sd'])[RANDOM['rand_num']].click()


	
