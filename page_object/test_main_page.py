from selenium.webdriver.common.by import By
from selenium import webdriver
from page_object.test_base_page import BasePage


class Test_main_page_locators:
    visible_element_main_page = (By.CSS_SELECTOR, '[id = "slider_row"]')
    button_cart = (By.CSS_SELECTOR, '.shopping_cart>a')
    button_cart_sign_in = (By.CSS_SELECTOR, 'a[class="login"]')
    woman_tab_loc = (By.CSS_SELECTOR, '[title="Women"]')
    woman_tab_element = (By.CSS_SELECTOR, '[class="content_scene_cat"]')


class Test_main(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php'

    def check_for_expectation(self):
        assert self.find_element(Test_main_page_locators.visible_element_main_page).is_displayed()

    def clicking_the_shopping_cart_button(self):
        self.click_element(Test_main_page_locators.button_cart)

    def clicking_the_shopping_sign_in_button(self):
        self.click_element(Test_main_page_locators.button_cart_sign_in)

    def woman_tab(self):
        self.click_element(Test_main_page_locators.woman_tab_loc)
        assert self.find_element(Test_main_page_locators.woman_tab_loc).is_displayed()