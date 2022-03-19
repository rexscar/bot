from booking.booking import Booking
from time import sleep


try:
    with Booking(teardown=True) as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go("New York")
        bot.select_dates(checkin_date='2022-03-20'
                         , checkout_date='2022-03-25')
        bot.select_adults(5)
        bot.click_search()
        bot.filterbooking()
        bot.refresh()
        bot.report_results()
        # bot.testClipboard()



except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:\SeleniumDrivers \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
