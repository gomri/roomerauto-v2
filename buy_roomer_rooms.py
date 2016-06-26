import re
import sys
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from Vars import *
from error_handling import *
from list_handling import *
from review_handling_N_thankyou import *
from entry_handling import *




#--------------------------------- SETUP DRIVER AND SETTINGS ---------------------
class setup_for_tests(object):
	def setup_driver(self):
		driver = webdriver.Firefox()
		driver.implicitly_wait(DRIVER_SETTINGS['wait'])
		return driver

# # -------------------------- test buy rooms from kayak


# #------------------------------- test search rooms on roomer ----------------------
def buy_roomer_choose_destination(driver):
	driver.get(ROOMER['url'].format(env='qa-2'))
	driver.find_element_by_css_selector(HOME_PAGE['search_rooms']['choose_destination']['selector']).send_keys(HOME_PAGE['search_rooms']['choose_destination']['data_to_fill'])
	driver.find_element_by_css_selector(HOME_PAGE['search_rooms']['choose_destination']['click_dropdown']).click()
	sleep(2)
	driver.find_element_by_name(HOME_PAGE['search_rooms']['choose_check_in']['selector']).click()
	driver.find_element_by_css_selector(HOME_PAGE['search_rooms']['choose_check_in']['check_in_date'].format(date=DATE['the_date_in_3_days'])).click()
	driver.find_element_by_css_selector(HOME_PAGE['search_rooms']['click_find_rooms']).click()

	unlock_SD(driver)
	click_random_room(driver)
	driver.switch_to.window(driver.window_handles[-1])
	try:
		cancellation_policy,supplier_type = click_FC(driver)
	except NoSuchElementException:
		cancellation_policy,supplier_type = click_NR(driver)
	sleep(5)
	fill_in_review_page(driver)
	tested = expect_thankyou_page(driver)

	print_test_report(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_search_rooms_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested)

	insert_data_to_dict(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_search_rooms_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested,
						TEST_TO_RUN['roomer_search_rooms_open_sd_buy_random'])

# #------------------------------ test secret deal on roomer -----------------------
def buy_roomer_secret_deal(driver):
	driver.get(ROOMER['url'].format(env='qa-2')) # Setting the testing env

	driver.find_element_by_css_selector(HOME_PAGE['secret_deal']).click()

	unlock_SD(driver)
	click_random_room(driver)
	driver.switch_to.window(driver.window_handles[-1])
	try:
		cancellation_policy,supplier_type = click_FC(driver)
	except NoSuchElementException:
		cancellation_policy,supplier_type = click_NR(driver)
	sleep(5)
	fill_in_review_page(driver)
	tested = expect_thankyou_page(driver)

	print_test_report(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_sd_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested)

	insert_data_to_dict(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_sd_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested,
						TEST_TO_RUN['roomer_buy_random_from_sd_with_sd_open'])


# # ------------------------------ test top 100 on roomer -----------------------
def buy_roomer_top_100(driver):
	driver.get(ROOMER['url'].format(env='qa-2'))

	driver.find_element_by_css_selector(HOME_PAGE['top_100']).click()
	driver.find_element_by_css_selector(TOP_100_PAGE['san-diego']).click()

	unlock_SD(driver)
	click_random_room(driver)
	driver.switch_to.window(driver.window_handles[-1])
	try:
		cancellation_policy,supplier_type = click_LH(driver)
	except NoSuchElementException:
		cancellation_policy,supplier_type = click_FC(driver)
	sleep(5)
	fill_in_review_page(driver)
	tested = expect_thankyou_page(driver)

	print_test_report(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_top_100_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested)

	insert_data_to_dict(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_top_100_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested,
						TEST_TO_RUN['roomer_top_100_open_sd_buy_random'])

# #--------------------------- last minute deals roomer open sd --------------------
def buy_roomer_last_minute_deals(driver):
	driver.get(ROOMER['url'].format(env='qa-2'))

	driver.find_element_by_id(HOME_PAGE['last_minute_deals']).click()

	unlock_SD(driver)
	click_random_room(driver)
	driver.switch_to.window(driver.window_handles[-1])
	try:
		cancellation_policy,supplier_type = click_FC(driver)
	except NoSuchElementException:
		cancellation_policy,supplier_type = click_NR(driver)
	sleep(5)
	fill_in_review_page(driver)
	tested = expect_thankyou_page(driver)

	print_test_report(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_last_minute_deals_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested)

	insert_data_to_dict(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_last_minute_deals_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested,
						TEST_TO_RUN['roomer_last_minute_deals_open_sd_buy_random'])

# #------------------- discover cities to visit open sd ----------------------
def buy_roomer_discover_cities(driver):	
	driver.get(ROOMER['url'].format(env='qa-2'))

	driver.find_element_by_css_selector(HOME_PAGE['discover_cities']).click()

	unlock_SD(driver)
	click_random_room(driver)
	driver.switch_to.window(driver.window_handles[-1])
	try:
		cancellation_policy,supplier_type = click_LH(driver)
	except NoSuchElementException:
		cancellation_policy,supplier_type = click_FC(driver)
	sleep(5)
	fill_in_review_page(driver)
	tested = expect_thankyou_page(driver)

	print_test_report(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_discover_cities_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested)

	insert_data_to_dict(TEST_CASE_PARAMS['source_roomer'],
						TEST_CASE_PARAMS['test_cases']['roomer_discover_cities_open_sd_buy_random'],
						cancellation_policy,
						supplier_type,
						tested,
						TEST_TO_RUN['roomer_discover_cities_open_sd_buy_random'])

	def clean_up(driver):
		driver.quit()	
