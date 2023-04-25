import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkbox():
    chrome = webdriver.Chrome()
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    chrome.get(url=url)
    checkbox = chrome.find_element(By.CSS_SELECTOR, '[type="checkbox"][label="blah"]')
    checkbox_button = WebDriverWait(chrome, 15).until(EC.element_to_be_clickable(checkbox))
    checkbox_button.click()
    message_locator = chrome.find_element(By.XPATH, '//p[@id="message"]')
    message = WebDriverWait(chrome, 15).until(EC.presence_of_element_located(message_locator))
    assert message.text == "It’s gone!"
    assert not checkbox_button._is_selected()
    input_button_enable = chrome.find_element(By.CSS_SELECTOR, '[type="button"][onclick="swapInput()"]')
    enable = WebDriverWait(chrome, 15).until(EC.element_to_be_clickable(input_button_enable))
    enable.click()
    assert enable.is_disable()
    input_button_disable = chrome.find_element(By.CSS_SELECTOR, '[type="button"][onclick="swapCheckbox()"]')
    disable = WebDriverWait(chrome, 15).until(EC.element_to_be_clickable(input_button_disable))
    disable.click()
    message_2_locator = chrome.find_element(By.CSS_SELECTOR, '[id="message"]')
    message_2 = WebDriverWait(chrome, 15).until(EC.presence_of_element_located(message_2_locator))
    assert message_2.text == "It's enabled!"
    assert disable.is_enable()
    time.sleep(15)