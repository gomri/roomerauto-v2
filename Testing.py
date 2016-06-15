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
from review_handling_N_thankyou import *
from entry_handling import *




driver = webdriver.Firefox()
driver.implicitly_wait(DRIVER_SETTINGS['wait'])

driver.get(URL['base'].format(env='qa-1')) # Setting the testing env

driver.find_element_by_css_selector(HOME_PAGE['secret_deal']).click()
# driver.find_element_by_css_selector(TOP_100_PAGE['san-diego']).click()

unlock_SD(driver)
click_random_room(driver)
driver.switch_to.window(driver.window_handles[-1])
try:
	cancellation_policy,supplier_type = click_FC(driver)
except NoSuchElementException:
	cancellation_policy,supplier_type = click_NR(driver)
sleep(5)
# url = str(driver.current_url)
fill_in_review_page(driver)
tested = expect_thankyou_page(driver)

print_test_report(TEST_CASE_PARAMS['source_roomer'],
					TEST_CASE_PARAMS['test_cases']['roomer_sd_open_sd_buy_random'],
					cancellation_policy,
					supplier_type,
					tested)