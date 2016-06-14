import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from Vars import *
from error_handling import *
from time import sleep
from list_handling import *
from review_handling import *
from entry_handling import *



driver = webdriver.Firefox()
driver.implicitly_wait(DRIVER_SETTINGS['wait'])

driver.get(URL['base'].format(env='qa-1')) # Setting the testing env

driver.find_element_by_css_selector(HOME_PAGE['secret_deal']).click()
# driver.find_element_by_css_selector(TOP_100_PAGE['san-diego']).click()

unlock_SD(driver)
click_random_room(driver)
driver.switch_to.window(driver.window_handles[-1])
click_FC(driver)
sleep(5)
# url = str(driver.current_url)
fill_in_review_page(driver)