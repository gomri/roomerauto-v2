from Vars import REVIEW_PAGE
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


def fill_in_review_page(driver,url=None):
	if url:
		driver.get(url)
	try:   
		review_with_LH = driver.find_element_by_css_selector(".lh-select.collapsable.font-regular.bottom-separator")
		review_with_LH.find_element_by_xpath(u"//span[contains(text(), '(Recommended)')]").click()
		review_with_LH.find_element_by_css_selector('.continue-button.standard-button.smaller.font-regular.weight-medium.push-bottom').click()
	except NoSuchElementException:
	  	pass
	insert_review_full_name = driver.find_element_by_id(REVIEW_PAGE['fill_in_full_name']['id_selector']).send_keys(REVIEW_PAGE['fill_in_full_name']['data_to_fill'])
	insert_review_mobile_number = driver.find_element_by_id(REVIEW_PAGE['fill_in_mobile']['id_selector']).send_keys(REVIEW_PAGE['fill_in_mobile']['data_to_fill'])
	insert_review_email = driver.find_element_by_id(REVIEW_PAGE['fill_in_email']['id_selector']).send_keys(REVIEW_PAGE['fill_in_email']['data_to_fill'])
	click_continue_review_step2 = driver.find_element_by_link_text(REVIEW_PAGE['contiune']).click()
	insert_credit_number_review = driver.find_element_by_id(REVIEW_PAGE['fill_in_credit_card']['id_selector']).send_keys(REVIEW_PAGE['fill_in_credit_card']['data_to_fill'])
	insert_credit_expire_date_review = driver.find_element_by_id(REVIEW_PAGE['fill_in_credit_expire_date']['id_selector']).send_keys(REVIEW_PAGE['fill_in_credit_expire_date']['data_to_fill'])
	insert_credit_expire_year_review = driver.find_element_by_id(REVIEW_PAGE['fill_in_credit_card_epire_year']['id_selector']).send_keys(REVIEW_PAGE['fill_in_credit_card_epire_year']['data_to_fill'])
	insert_credit_4last_num_review = driver.find_element_by_id(REVIEW_PAGE['fill_in_credit_card_4last_digits']['id_selector']).send_keys(REVIEW_PAGE['fill_in_credit_card_4last_digits']['data_to_fill'])
	insert_billing_address_text = driver.find_element_by_id(REVIEW_PAGE['fill_in_billing_address']['id_selector']).send_keys(REVIEW_PAGE['fill_in_billing_address']['data_to_fill'])
	insert_billing_address_click_box = driver.find_element_by_id(REVIEW_PAGE['fill_in_billing_address']['id_selector']).click()
	insert_billing_address_arrow_down = driver.find_element_by_id(REVIEW_PAGE['fill_in_billing_address']['id_selector']).send_keys(REVIEW_PAGE['fill_in_billing_address']['click_arrow_down'])
	insert_billing_address_click_enter = driver.find_element_by_id(REVIEW_PAGE['fill_in_billing_address']['id_selector']).send_keys(REVIEW_PAGE['fill_in_billing_address']['click_enter'])
	insert_zip_code = driver.find_element_by_id(REVIEW_PAGE['fill_in_zip_code']['id_selector']).send_keys(REVIEW_PAGE['fill_in_zip_code']['data_to_fill'])
	click_book_button_review = driver.find_element_by_css_selector(REVIEW_PAGE['complete_booking']).click()
	