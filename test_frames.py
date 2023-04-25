import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_flames():
    chrome = webdriver.Chrome()
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    chrome.get(url=url)
    field = chrome.find_element(By.CSS_SELECTOR, '[id="tinymce"][class="mce-content-body "]')
    assert field.is_selected()
    message_field = chrome.find_element(By.XPATH, '//body/p')
    message = WebDriverWait(chrome, 15).until(EC.presence_of_element_located(message_field))
    assert message.text == 'Your content goes here.'
    time.sleep(15)