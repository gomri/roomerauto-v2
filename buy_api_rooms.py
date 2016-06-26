import requests
import json
import re 
import time
from selenium.common.exceptions import NoSuchElementException
from entry_handling import * 
from review_handling_N_thankyou import *
from list_handling import *
from API_requests import *
from Vars import *
from global_functions import *
from selenium import webdriver


class API_request(object):
    """
        make request to roomer api with different headers 
        as different partners
        and check connection is valid and that is resived 
    """
    def __init__(self, header, url):
        self.header = header
        self.url = url

    def Connect_to_api(self):
        try:
            response = requests.get(self.url, params=None, headers=self.header)
        except requests.exceptions.Timeout:
            response = requests.get(self.url, params=None,headers=self.header)
        except requests.exceptions.TooManyRedirects:
            print 'URL was bad try a different one'
        except requests.exceptions.RequestException as e:
            print e
            sys.exit(1)
        return response

    def get_rooms_url(self, response_content):
        _json_response_content = json.loads(response_content)
        list_of_reservation_urls = []
        for i in range(len(_json_response_content)):
            room_mate_redirect = _json_response_content[i]['reservation']['url']
            list_of_reservation_urls.append(get_redirect_url(REGEX['find_meta_redirect'], 
                                                                    room_mate_redirect, 
                                                                    ROOMER['url'].format(env='qa-2')))
        return list_of_reservation_urls

def buy_api_rooms(driver, header=None, url=None, partner_name=None, buy_from_list=True):
    kayak_rooms = API_request(header, url)
    response_status = kayak_rooms.Connect_to_api().status_code
    response_content = kayak_rooms.Connect_to_api().content
    if response_status == 200:
        list_of_room_urls = kayak_rooms.get_rooms_url(response_content)
        if len(list_of_room_urls) >= API['max_reservation_to_buy']: # set how what is the max amount of reservation to buy if the api request return aloot of rooms
            amount_rooms_to_buy = API['max_reservation_to_buy']
        else:
            amount_rooms_to_buy = len(list_of_room_urls)
        for i in range(amount_rooms_to_buy):
            driver.get(list_of_room_urls[i])
            if buy_from_list == True:
                try:
                    click_highlighted(driver)
                    driver.switch_to.window(driver.window_handles[-1])
                except Exception:
                    continue
            elif buy_from_list == False:
                pass
            source = get_source(REGEX['find_source'], driver.current_url)
            try:
                cancellation_policy,supplier_type = click_FC(driver)
            except NoSuchElementException:
                cancellation_policy,supplier_type = click_NR(driver)
            sleep(5)
            fill_in_review_page(driver)
            sleep(5)
            tested = expect_thankyou_page(driver)
            driver.switch_to.window(driver.window_handles[-1])

            print_test_report(source,
                                TEST_CASE_PARAMS['test_cases']['from_partner_buy_all_api_request_reservations'].
                                                                                                                format(partner=partner_name),
                                cancellation_policy,
                                supplier_type,
                                tested)

            insert_data_to_dict(source,
                                TEST_CASE_PARAMS['test_cases']['from_partner_buy_all_api_request_reservations'].
                                                                                                                format(partner=partner_name),
                                cancellation_policy,
                                supplier_type,
                                tested,
                                TEST_TO_RUN['from_partner_buy_all_api_request_reservations'])

        driver.quit()

    else:
        print 'There was a problem with your request it returned', response_status

