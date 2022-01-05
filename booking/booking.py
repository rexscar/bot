from selenium import webdriver
import os
import clipboard
import booking.constants as const
from booking.booking_filter import Bookingfiltration
from selenium.webdriver.common.by import By
from booking.booking_report import BookingReport
from selenium.webdriver.common.keys import Keys
from time import sleep


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_results = self.find_element(
            By.CSS_SELECTOR, 'li[data-i="0"]'
        )
        first_results.click()

    def select_dates(self, checkin_date, checkout_date):
        checkin_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{checkin_date}"]'
        )
        checkin_element.click()
        checkout_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{checkout_date}"]'
        )
        checkout_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(By.ID, 'xp__guests__toggle')
        selection_element.click()

        decrease_adult_element = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]'
        )
        adult_count_element = self.find_element(By.ID, "group_adults")
        adult_count_value = adult_count_element.get_attribute('value')

        while int(adult_count_value) != 1:
            decrease_adult_element.click()
            adult_count_value = adult_count_element.get_attribute('value')

        increase_adult_element = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count-1):
            increase_adult_element.click()

    def click_search(self):
        click_submit_element = self.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        )
        click_submit_element.click()

    def filterbooking(self):
        filtration = Bookingfiltration(driver=self)
        filtration.sort_lowest_first()
        filtration.apply_star_rating(3, 4, 5)

    def report_results(self):
        hotel_boxes = self.find_element(
            By.ID, "search_results_table"
        )
        report = BookingReport(hotel_boxes)
        print(report.pull_deal_box_attributes())

    def testClipboard(self):
        search_field = self.find_element(By.ID, "ss")
        search_field.clear()
        clipboard.copy('GoDigiS@stanbic.com.gh')
        search_field.click()
        sleep(10)
        search_field.send_keys(Keys.CONTROL, 'v')
        sleep(10)
        #fill.send_keys(Keys.RETURN)
        clipboard.copy('Ghana@123')




