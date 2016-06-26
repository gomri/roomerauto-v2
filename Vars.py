from selenium.webdriver.common.keys import Keys
from random import randint as random_num
import datetime
from global_functions import *

DATE = {
	'the_date_in_3_days':get_date()
}

RANDOM = {
	'rand_num': random_num(1,5)
}

ROOMER = {
	'url':'http://roomer-{env}.herokuapp.com' # env = testing enviorment
}

REGEX = {
	'find_supplier_type':'(&t=)(\w)',
	'find_meta_redirect':'(\/meta_redirect.*)',
	'find_source':'(utm_source=)(\w+)'
}

PARTNERS = {
	'kayak':'kayak',
	'skyscanner':'skyscanner',
	'trivago':'trivago'
}

API = {
	'url':'http://roomer-api-{env}.herokuapp.com/api/reservations_by_hotels/{hotel_id}/{check_in}/{check_out}',
	'hotel_id': get_hotel_id(),
	'check_in': get_check_in(),
	'check_out': get_check_out(),
	'request_headers':{
		'authorization':{
			'key':'Authorization',
			'value':'Token token={token}'
		},
		'partner':{
			'key':'partner',
			'value':'{email}'
		},
		'api-version':{
			'key':'API-Version',
			'value':'1'
		},
	},
	'email-token_pars':{
		'kayak':{
			'token_one':'cd7de248487ac667fe3a6f60235ed1d0',
			'token_two':None,
			'email':'eric@kayak.com'
		},
		'trivago':{
			'token_one':'3db72ddafd7e149ec1edf659949ed6d0',
			'token_two':None,
			'email':'trivago-test@roomertravel.com'
		},
	'skyscanner':{
			'token_one':'5ac8ffca9b0b36a14ac526ffb7a4753b',
			'token_two':None,
			'email':'ashleigh.cruickshank@skyscanner.net'
		},
	},
	'max_reservation_to_buy':3
}

KAYAK_HEADER = {
    API['request_headers']['authorization']['key']: API['request_headers']['authorization']['value'].format(
                                                                    token=API['email-token_pars']['kayak']['token_one']
                                                                    ),
    API['request_headers']['partner']['key']: API['request_headers']['partner']['value'].format(
                                                                    email=API['email-token_pars']['kayak']['email']
                                                                    ),
    API['request_headers']['api-version']['key']: API['request_headers']['api-version']['value']
}

SKYSCANNER_HEADER = {
    API['request_headers']['authorization']['key']: API['request_headers']['authorization']['value'].format(
                                                                    token=API['email-token_pars']['skyscanner']['token_one']
                                                                    ),
    API['request_headers']['partner']['key']: API['request_headers']['partner']['value'].format(
                                                                    email=API['email-token_pars']['skyscanner']['email']
                                                                    ),
    API['request_headers']['api-version']['key']: API['request_headers']['api-version']['value']
}

TRIVAGO_HEADER = {
    API['request_headers']['authorization']['key']: API['request_headers']['authorization']['value'].format(
                                                                    token=API['email-token_pars']['trivago']['token_one']
                                                                    ),
    API['request_headers']['partner']['key']: API['request_headers']['partner']['value'].format(
                                                                    email=API['email-token_pars']['trivago']['email']
                                                                    ),
    API['request_headers']['api-version']['key']: API['request_headers']['api-version']['value']
}

URL_FOR_API_REQUESTS = API['url'].format(
		env='qa-2',
		hotel_id=API['hotel_id'],
		check_in=API['check_in'],
		check_out=API['check_out']
	)


HOME_PAGE = {
	'secret_deal':'.find_rooms.blue-btn',
	'sell':'.sell',
	'last_minute_deals':'last_minute_deals_link',
	'top_100':'.event',
	'discover_cities':'.three.columns.rmr-img-sprite.rmr-img-cities',
	'search_rooms':{
		'choose_destination':{
			'selector':'.text.input.tt-query',
			'data_to_fill':'london',
			'click_dropdown':'.tt-suggestions .tt-suggestion'
		},
		'choose_check_in':{
			'selector':'check-in',
			'check_in_date':'td[data-day="{date}"]'
		},
		'click_find_rooms':'.find_rooms.blue-btn'
	}
}


TOP_100_PAGE = {
	'new_york':'a[href*="Las-Vegas"]',
	'san-diego':'a[href*="San-Diego"]',
}

LIST_PAGE = {	
	'index_all_rooms_non_sd':'.component-card-inner.component-inner',
	'click_room_non_sd':'a[href*="/hotels"]',
	'unlock_secret_deal':{
		'parent_element':'.secret_deal_banner.secret_deal_login.clearfix',
		'select_input_field':'input[name="user[email]"]',
		'data_to_fill':'bob.g@goog.com',
		'click_unlock':'button'
	}
}

ENTRY_PAGE = {
	'click_book':'.standard-button.proceed_to_checkout',
	'click_FC':'.button.proceed_to_checkout',
	'click_NR':'.clearfix.component_items.protection_items.non_refundable_items',
	'click_LH':'.clearfix.component_items.protection_items.life_happens_items'
	# ----------------------- not working ----------------------
	# 'unlock_secret_deal':{ 
	# 	'click_to_input_email':'.button.secret_deal_unlock',
	# 	'fill_in_box':'user_email',
	# 	'data_to_fill':'bob.g@bob.g.com',
	# 	'click_unlock':'button'
	# }
}

REVIEW_PAGE = {
	'fill_in_full_name': {
		'id_selector':'review-full-name',
		'data_to_fill':'omri golan'
	},
	'fill_in_mobile': {
		'id_selector':'mobile-number',
		'data_to_fill':'7547541452'
	},
	'fill_in_email':{
		'id_selector':'review-email',
		'data_to_fill':'bob.g@goroomer.com'
	},
	'contiune':'Continue',
	'fill_in_credit_card':{
		'id_selector':'review-credit-card-number',
		'data_to_fill':'4242424242424242'
	},
	'fill_in_credit_expire_date':{
		'id_selector':'review-cc-exp-month',
		'data_to_fill':Keys.PAGE_DOWN
	},
	'fill_in_credit_card_epire_year':{
		'id_selector':'review-cc-exp-year',
		'data_to_fill':Keys.PAGE_DOWN
	},
	'fill_in_credit_card_4last_digits':{
		'id_selector':'review-cc-security-code',
		'data_to_fill':'789'
	},
	'fill_in_billing_address':{
		'id_selector':'billing-address-input',
		'data_to_fill':'Israel Post, Dizengoff Street, Tel Aviv-Yafo',
		'click_arrow_down':Keys.ARROW_DOWN,
		'click_enter':Keys.ENTER
	},
	'fill_in_zip_code':{
		'id_selector':'review-zip',
		'data_to_fill':'3187'
	},
	'complete_booking':'.complete-booking.weight-bold'
}


THANKYOU_PAGE = {
	'thankyou_title':'.thank_you_title'
}

SCREEN_SHOT = {
	'screen_shot_name':'{screen_shot_name}.png'
}

DRIVER_SETTINGS = {
	'wait':20
}

TEST_CASE_PARAMS = {
	'source_roomer':'roomer',
	'test_cases':{
		'roomer_search_rooms_open_sd_buy_random':'roomer ->search rooms ->open secret deal ->buy random',
		'roomer_sd_open_sd_buy_random':'roomer ->secret deal ->open secret deal ->buy random',
		'roomer_top_100_open_sd_buy_random':'roomer ->top 100 ->open secret deal ->buy random',
		'roomer_last_minute_deals_open_sd_buy_random':'roomer ->last minute deals ->open secret deal ->buy random',
		'roomer_discover_cities_open_sd_buy_random':'roomer ->discover cities ->open secret deal ->buy random',
		'from_partner_buy_all_api_request_reservations':'{partner}(api) ->list ->buy all rooms returned from request'
	}
}

TEST_TO_RUN = {
	'roomer_buy_random_from_sd_with_sd_open':{
		'source':'{source}',
		'test_case':'{test_case}',
		'supplier_type':'{supplier_type}',
		'cancellation_policy':'{cancellation_policy}',
		'tested':False
	},
	'roomer_top_100_open_sd_buy_random':{
		'source':'{source}',
		'test_case':'{test_case}',
		'supplier_type':'{supplier_type}',
		'cancellation_policy':'{cancellation_policy}',
		'tested':False
	},
	'roomer_last_minute_deals_open_sd_buy_random':{
		'source':'{source}',
		'test_case':'{test_case}',
		'supplier_type':'{supplier_type}',
		'cancellation_policy':'{cancellation_policy}',
		'tested':False
	},
	'roomer_discover_cities_open_sd_buy_random':{
		'source':'{source}',
		'test_case':'{test_case}',
		'supplier_type':'{supplier_type}',
		'cancellation_policy':'{cancellation_policy}',
		'tested':False
	},
	'roomer_search_rooms_open_sd_buy_random':{
		'source':'{source}',
		'test_case':'{test_case}',
		'supplier_type':'{supplier_type}',
		'cancellation_policy':'{cancellation_policy}',
		'tested':False
	},
	'from_partner_buy_all_api_request_reservations':{
		'source':'{source}',
		'test_case':'{test_case}',
		'supplier_type':'{supplier_type}',
		'cancellation_policy':'{cancellation_policy}',
		'tested':False
	},
}


# 	'buy_roomer_p2p_NR_rate_1': {
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_p2p_FC_rate_1':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_p2p_LH_rate_1':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_p2p_NR_rate_2':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_p2p_FC_rate_2':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_p2p_LH_rate_2':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_smartp2p_NR':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_smartp2p_LH':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_expedia_NR':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_expedia_FC':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_expedia_LH':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_torico_NR':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_torico_FC':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_torico_LH':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_hotelbeds_NR':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_hotelbeds_FC':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_roomer_hotelbeds_LH':{
# 		'tested': False,
# 		'room_url': None
# 	},
# 	'buy_kayak_p2p_NR_rate_1':False,
# 	'buy_kayak_p2p_FC_rate_1':False,
# 	'buy_kayak_p2p_LH_rate_1':False,
# 	'buy_kayak_p2p_NR_rate_2':False,
# 	'buy_kayak_p2p_FC_rate_2':False,
# 	'buy_kayak_p2p_LH_rate_2':False,
# 	'buy_kayak_smartp2p_NR_rate_1':False,
# 	'buy_kayak_smartp2p_LH_rate_1':False,
# 	'buy_kayak_smartp2p_NR_rate_2':False,
# 	'buy_kayak_smartp2p_LH_rate_2':False,
# 	'buy_kayak_torico_NR_rate_1':False,
# 	'buy_kayak_torico_FC_rate_1':False,
# 	'buy_kayak_torico_LH_rate_1':False,
# 	'buy_kayak_torico_NR_rate_2':False,
# 	'buy_kayak_torico_FC_rate_2':False,
# 	'buy_kayak_torico_LH_rate_2':False,
# 	'buy_kayak_hotelbeds_NR_rate_1':False,
# 	'buy_kayak_hotelbeds_FC_rate_1':False,
# 	'buy_kayak_hotelbeds_LH_rate_1':False,
# 	'buy_kayak_hotelbeds_NR_rate_2':False,
# 	'buy_kayak_hotelbeds_FC_rate_2':False,
# 	'buy_kayak_hotelbeds_LH_rate_2':False,
# 	'buy_skyscanner_p2p_NR_rate_2':False,
# 	'buy_skyscanner_p2p_FC_rate_2':False,
# 	'buy_skyscanner_p2p_LH_rate_2':False,
# 	'buy_skyscanner_smartp2p_NR_rate_2':False,
# 	'buy_skyscanner_smartp2p_LH_rate_2':False,
# 	'buy_skyscanner_torico_NR_rate_2':False,
# 	'buy_skyscanner_torico_FC_rate_2':False,
# 	'buy_skyscanner_torico_LH_rate_2':False,
# 	'buy_skyscanner_hotelbeds_NR_rate_2':False,
# 	'buy_skyscanner_hotelbeds_FC_rate_2':False,
# 	'buy_skyscanner_hotelbeds_LH_rate_2':False,
# 	'buy_skyscanner_expedia_NR_rate_2':False,
# 	'buy_skyscanner_expedia_FC_rate_2':False,
# 	'buy_skyscanner_expedia_LH_rate_2':False,
# 	'buy_trivago_p2p_NR_rate_2':False,
# 	'buy_trivago_p2p_FC_rate_2':False,
# 	'buy_trivago_p2p_LH_rate_2':False,
# 	'buy_trivago_smartp2p_NR_rate_2':False,
# 	'buy_trivago_smartp2p_LH_rate_2':False,
# 	'buy_trivago_torico_NR_rate_2':False,
# 	'buy_trivago_torico_FC_rate_2':False,
# 	'buy_trivago_torico_LH_rate_2':False,
# 	'buy_trivago_hotelbeds_NR_rate_2':False,
# 	'buy_trivago_hotelbeds_FC_rate_2':False,
# 	'buy_trivago_hotelbeds_LH_rate_2':False
# }