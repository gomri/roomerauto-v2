import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from Vars import *
from error_handleing import *
from time import sleep

def get_supplier_type(url, regex):
    string_supplier_type = re.search(regex, url).group(2)
    return string_supplier_type

driver = webdriver.Firefox()

driver.implicitly_wait(DRIVER_SETTINGS['wait'])
driver.get(URL['base'].format(env='qa-1')) # Setting the testing env

driver.find_element_by_css_selector(HOME_PAGE['top_100']).click()
driver.find_element_by_css_selector(TOP_100_PAGE['san-diego']).click()
for i in range(20):
	try:
		room_url = driver.find_elements_by_css_selector(LIST_PAGE['click_room_non_sd'])[i].get_attribute('href')
		# driver.get(room_url)
		print get_supplier_type(room_url,REGEX['find_suuplier_type'])
	except Exception:
		driver.refresh()
# driver.quit()