# this file will include a class with instance method to apply filtration
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Bookingfiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.XPATH, '//*[@id="searchboxInc"]/div[1]/div/div/div[1]/div[5]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars' :
                    star_element.click()

    def sort_lowest_first(self):
        sort_element = self.driver.find_element(
            By.CSS_SELECTOR, 'li[data-id="price"]'
        )
        sort_element.click()