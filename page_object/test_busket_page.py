from selenium.webdriver.common.by import By
from selenium import webdriver
from page_object.test_base_page import BasePage


class Test_busket_page_locators:
    locator_cart_is_empty = (By.CSS_SELECTOR, '.alert.alert-warning')
    locator_exit = (By.CSS_SELECTOR, 'a[class="home"]')


class Test_busket(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php?controller=order'

    def checking_cart_for_expectation(self):
        assert self.url == self.webdriver.current_url

    def cart_is_empty(self):
        assert self.find_element(Test_busket_page_locators.locator_cart_is_empty).text == 'Your shopping cart is empty.'

    def exit_to_main_page(self):
        self.click_element(Test_busket_page_locators.locator_exit)