from selenium.webdriver.common.keys import Keys
from random import randint as random_num

RANDOM = {
	'rand_num': random_num(1,10)
}

URL = {
	'base':'http://roomer-{env}.herokuapp.com' # env = testing enviorment
}

REGEX = {
	'find_supplier_type':'(&t=)(\w)'
}

API = {
	'base':'http://roomer-api-{env}.herokuapp.com/api/reservations_by_hotels/{hotel_id}/{check_in}/{check_out}'
}

HOME_PAGE = {
	'secret_deal':'.find_rooms.blue-btn',
	'sell':'.sell',
	'last_minute_deals':'last_minute_deals_link',
	'top_100':'.event',
	'discover_cities':'.three.columns.rmr-img-sprite.rmr-img-cities'
}

TOP_100_PAGE = {
	'new_york':'a[href*="Las-Vegas"]',
	'san-diego':'a[href*="San-Diego"]',
}

LIST_PAGE = {	
	'index_all_rooms_non_sd':'.component-card-inner.component-inner',
	'click_room_non_sd':'.component-content.component-card-content.component-post'
}

ENTRY_PAGE = {
	'book_button_FC':'.button.proceed_to_checkout',
	'unlock_secret_deal':{
		'click_to_input_email':'.button.secret_deal_unlock',
		'fill_in_box':'user_email',
		'data_to_fill':'bob.g@bob.g.com',
		'click_unlock':'button'
	}
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
		'data_to_fill':'2179'
	},
	'fill_in_billing_address':{
		'id_selector':'billing-address-input',
		'data_to_fill':'Israel',
		'click_arrow_down':Keys.ARROW_DOWN,
		'click_enter':Keys.ENTER
	},
	'fill_in_zip_code':{
		'id_selector':'review-zip',
		'data_to_fill':'3187'
	},
	'complete_booking':'.complete-booking.weight-bold'
}

SCREEN_SHOT = {
	'screen_shot_name':'{screen_shot_name}.png'
}

DRIVER_SETTINGS = {
	'wait':15
}

TEST_TO_RUN = {
	'buy_roomer_p2p_NR_rate_1': {
		'tested': False,
		'room_url': None
	},
	'buy_roomer_p2p_FC_rate_1':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_p2p_LH_rate_1':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_p2p_NR_rate_2':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_p2p_FC_rate_2':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_p2p_LH_rate_2':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_smartp2p_NR':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_smartp2p_LH':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_expedia_NR':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_expedia_FC':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_expedia_LH':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_torico_NR':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_torico_FC':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_torico_LH':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_hotelbeds_NR':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_hotelbeds_FC':{
		'tested': False,
		'room_url': None
	},
	'buy_roomer_hotelbeds_LH':{
		'tested': False,
		'room_url': None
	},
	'buy_kayak_p2p_NR_rate_1':False,
	'buy_kayak_p2p_FC_rate_1':False,
	'buy_kayak_p2p_LH_rate_1':False,
	'buy_kayak_p2p_NR_rate_2':False,
	'buy_kayak_p2p_FC_rate_2':False,
	'buy_kayak_p2p_LH_rate_2':False,
	'buy_kayak_smartp2p_NR_rate_1':False,
	'buy_kayak_smartp2p_LH_rate_1':False,
	'buy_kayak_smartp2p_NR_rate_2':False,
	'buy_kayak_smartp2p_LH_rate_2':False,
	'buy_kayak_torico_NR_rate_1':False,
	'buy_kayak_torico_FC_rate_1':False,
	'buy_kayak_torico_LH_rate_1':False,
	'buy_kayak_torico_NR_rate_2':False,
	'buy_kayak_torico_FC_rate_2':False,
	'buy_kayak_torico_LH_rate_2':False,
	'buy_kayak_hotelbeds_NR_rate_1':False,
	'buy_kayak_hotelbeds_FC_rate_1':False,
	'buy_kayak_hotelbeds_LH_rate_1':False,
	'buy_kayak_hotelbeds_NR_rate_2':False,
	'buy_kayak_hotelbeds_FC_rate_2':False,
	'buy_kayak_hotelbeds_LH_rate_2':False,
	'buy_skyscanner_p2p_NR_rate_2':False,
	'buy_skyscanner_p2p_FC_rate_2':False,
	'buy_skyscanner_p2p_LH_rate_2':False,
	'buy_skyscanner_smartp2p_NR_rate_2':False,
	'buy_skyscanner_smartp2p_LH_rate_2':False,
	'buy_skyscanner_torico_NR_rate_2':False,
	'buy_skyscanner_torico_FC_rate_2':False,
	'buy_skyscanner_torico_LH_rate_2':False,
	'buy_skyscanner_hotelbeds_NR_rate_2':False,
	'buy_skyscanner_hotelbeds_FC_rate_2':False,
	'buy_skyscanner_hotelbeds_LH_rate_2':False,
	'buy_skyscanner_expedia_NR_rate_2':False,
	'buy_skyscanner_expedia_FC_rate_2':False,
	'buy_skyscanner_expedia_LH_rate_2':False,
	'buy_trivago_p2p_NR_rate_2':False,
	'buy_trivago_p2p_FC_rate_2':False,
	'buy_trivago_p2p_LH_rate_2':False,
	'buy_trivago_smartp2p_NR_rate_2':False,
	'buy_trivago_smartp2p_LH_rate_2':False,
	'buy_trivago_torico_NR_rate_2':False,
	'buy_trivago_torico_FC_rate_2':False,
	'buy_trivago_torico_LH_rate_2':False,
	'buy_trivago_hotelbeds_NR_rate_2':False,
	'buy_trivago_hotelbeds_FC_rate_2':False,
	'buy_trivago_hotelbeds_LH_rate_2':False
}