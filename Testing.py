import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from Vars import *
from error_handling import *
from time import sleep
from review_handling import *
from entry_handling import *

def get_supplier_type(url, regex):
    string_supplier_type = re.search(regex, url).group(2)
    return string_supplier_type

driver = webdriver.Firefox()
driver.implicitly_wait(DRIVER_SETTINGS['wait'])

# driver.get(URL['base'].format(env='qa-1')) # Setting the testing env

# driver.find_element_by_css_selector(HOME_PAGE['top_100']).click()
# driver.find_element_by_css_selector(TOP_100_PAGE['san-diego']).click()
# try:
# 	driver.find_elements_by_css_selector(LIST_PAGE['click_room_non_sd'])[RANDOM['rand_num']].click()
# except Exception:
#  	driver.refresh()
#  	driver.find_element_by_css_selector(LIST_PAGE['click_room_non_sd']).click()
# driver.switch_to.window(driver.window_handles[-1])

url='http://roomer-qa-1.herokuapp.com/hotels/san-diego-hotels/wyndham-garden-san-diego-near-sea-world.h4459?pr_id=32&hotel_id=4459&check_in=2016-06-24&check_out=2016-06-26&t=H&room_type_id=DBT-U10-DX-RO-U10&adults=2&children=0&child_guests_ages=&location_id=93&provider=&redis_id=4459,2016-06-24,2016-06-26,H,DBT-U10-DX-RO-U10,,2,0,&rate_plan_id=2&rate_plan_token=4537af5bfba2e8f3b36991be48cc6070&'

driver.get(url)
open_secret_deal(driver,url)

sleep(5)
# url = str(driver.current_url)

# fill_in_review_page(driver,url)