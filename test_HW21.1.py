import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web():
    chrome = webdriver.Chrome()
    url = 'https://thedemosite.co.uk/savedata.php'
    chrome.get(url=url)
    chrome.maximize_window()
    email_input = chrome.find_element(By.CLASS_NAME, 'username')
    email_input.send_keys('tanya@gmail.com')
    password_input = chrome.find_element(By.CLASS_NAME, 'password')
    password_input.send_keys('12345678')
    button_save = chrome.find_element(By.XPATH, "//input[@value='save']")
    button_save.click()
    email_input.is_displayed()
    password_input.is_displayed()
    time.sleep(10)