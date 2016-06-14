from Vars import LIST_PAGE
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

def click_random_room(driver,url=None):
	try:
		driver.find_elements_by_css_selector(LIST_PAGE['click_room_non_sd'])[RANDOM['rand_num']].click()
	except Exception:
	 	driver.refresh()
	 	driver.find_element_by_css_selector(LIST_PAGE['click_room_non_sd']).click()