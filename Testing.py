import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from Vars import *

driver = webdriver.Firefox()

driver.get(URL['base'])

index_cities = driver.find_element_by_css_selector(HOME_PAGE['discover_cities'])
index_cities.find_element_by_css_selector
