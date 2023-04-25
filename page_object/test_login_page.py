from selenium.webdriver.common.by import By
from selenium import webdriver
from page_object.test_busket_page import  BasePage


class Test_login_page():
    locator_registered = (By.CSS_SELECTOR, 'form[id="login_form"]')
    locator_exit = (By.CSS_SELECTOR, 'a[class="home"]')
    button_create_account = (By.CSS_SELECTOR, '[id="SubmitCreate"]>span')
    text_error = (By.CSS_SELECTOR, '[id="create_account_error"] li')
    password1 = (By.CSS_SELECTOR, '[class="lost_password form-group"]>a')
    string_input = (By.CSS_SELECTOR, '[class="form-control"]')
    retrieve_password = (By.CSS_SELECTOR, '[class="submit"]>button')
    text_error2 = (By.CSS_SELECTOR, '[class="alert alert-danger"] li')


class Test_login(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php?controller=authentication&back=my-account'

    def login_page_check(self):
        assert self.url == self.webdriver.current_url

    def visibility_already_registered(self):
        assert self.find_element(Test_login_page.locator_registered).is_displayed()

    def create_an_account(self):
        press_button = self.click_element(Test_login_page.button_create_account)
        assert self.find_element(Test_login_page.text_error).text == 'Invalid email address.'

    def forgot_your_password(self):
        self.click_element(Test_login_page.password1)
        self.send_keys(Test_login_page.string_input, 'Tanya@mail.com')
        self.click_element(Test_login_page.retrieve_password)
        assert self.find_element(Test_login_page.text_error2).text == 'Invalid email address.'

    def exit_to_main_page(self):
        self.click_element(Test_login_page.locator_exit)