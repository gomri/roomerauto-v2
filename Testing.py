import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from Vars import *

driver = webdriver.Firefox()

driver.implicitly_wait(15)
driver.get(URL['base'].format(env='qa-1')) # Setting the testing env

driver.find_element_by_css_selector(HOME_PAGE['discover_cities']).click()
list_of_rooms = driver.find_elements_by_css_selector(LIST['index_all_rooms_non_sd'])
for room in range(len(list_of_rooms)):
	d = list_of_rooms[room].find_element_by_css_selector(LIST['click_room_non_sd']).get_attribute('href')
# 	print d
# print len(list_of_rooms)
# driver.quit()