from buy_roomer_rooms import *
from buy_api_rooms import *


if __name__ == '__main__':
	def main():
		start_time = time.time()
		setup = setup_for_tests() 
		DRIVER =  setup.setup_driver()

		buy_roomer_choose_destination(DRIVER)
		buy_roomer_secret_deal(DRIVER)
		buy_roomer_top_100(DRIVER)
		buy_roomer_last_minute_deals(DRIVER)
		buy_roomer_discover_cities(DRIVER)
		clean_up(DRIVER)

		buy_api_rooms(DRIVER ,KAYAK_HEADER ,URL_FOR_API_REQUESTS ,PARTNERS['kayak'])
		buy_api_rooms(DRIVER ,SKYSCANNER_HEADER ,URL_FOR_API_REQUESTS ,PARTNERS['skyscanner'])
		buy_api_rooms(DRIVER ,TRIVAGO_HEADER ,URL_FOR_API_REQUESTS ,PARTNERS['trivago'], buy_from_list=False)
		clean_up(DRIVER)
		print("--- %s seconds ---" % (time.time() - start_time))

main()
