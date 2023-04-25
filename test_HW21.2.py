import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web2():
    chrome = webdriver.Chrome()
    url = 'https://demoqa.com/text-box'
    chrome.get(url=url)
    chrome.maximize_window()
    full_name = chrome.find_element(By.ID, 'userName')
    full_name.send_keys('Tatsiana')
    email = chrome.find_element(By.ID, 'userEmail')
    email.send_keys('Tanya@gmail.com')
    current_address = chrome.find_element(By.ID, 'currentAddress')
    current_address.send_keys('Minsk')
    permanent_address = chrome.find_element(By.ID, 'permanentAddress')
    permanent_address.send_keys('Gomel')
    button_submit = chrome.find_element(By.ID, 'submit')
    button_submit.click()
    full_name.is_displayed()
    email.is_displayed()
    current_address.is_displayed()
    permanent_address.is_displayed()
    time.sleep(10)