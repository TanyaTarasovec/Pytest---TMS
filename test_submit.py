import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_web():
    chrome = webdriver.Chrome()
    url = 'https://ultimateqa.com/filling-out-forms/'
    chrome.get(url=url)
    chrome.maximize_window()
    one_name = chrome.find_element(By.NAME, 'et_pb_contact_name_0')
    one_name.send_keys('Tatsiana')
    one_message = chrome.find_element(By.ID, 'et_pb_contact_message_0')
    one_message.send_keys('Help')
    button_submit = chrome.find_element(By.NAME, 'et_builder_submit_button')
    button_submit.click()
    element = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_form_0 > div')
    string = element.getText('Thanks for contacting us')
    time.sleep(15)


def test_web2():
    chrome = webdriver.Chrome()
    url = 'https://ultimateqa.com/filling-out-forms/'
    chrome.get(url=url)
    chrome.maximize_window()
    two_name = chrome.find_element(By.NAME, 'et_pb_contact_name_0')
    two_name.send_keys('Tatsiana')
    button_submit = chrome.find_element(By.NAME, 'et_builder_submit_button')
    button_submit.click()
    element = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_form_1 > div.et-pb-contact-message > p')
    string = element.getText('Please, fill in the following fields')
    time.sleep(15)


def test_web3():
    chrome = webdriver.Chrome()
    url = 'https://ultimateqa.com/filling-out-forms/'
    chrome.get(url=url)
    chrome.maximize_window()
    two_message = chrome.find_element(By.ID, 'et_pb_contact_message_0')
    two_message.send_keys('Help')
    button_submit = chrome.find_element(By.NAME, 'et_builder_submit_button')
    button_submit.click()
    element = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_form_1 > div.et-pb-contact-message > p')
    string = element.getText('Please, fill in the following fields')
    time.sleep(15)