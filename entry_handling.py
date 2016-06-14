from Vars import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from error_handleing import *

def click_FC(driver,url=None):
	driver.find_element_by_css_selector(ENTRY_PAGE['book_button_FC']).click()

