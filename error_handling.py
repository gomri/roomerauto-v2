from Vars import SCREEN_SHOT

def error_handler(driver,picture_name):
	driver.save_screenshot(SCREEN_SHOT['screen_shot_name'].format(screen_shot_name=picture_name))
	print '''There was an error a printscreen of the moment of the error was taken
	look in the script diractory to see it'''