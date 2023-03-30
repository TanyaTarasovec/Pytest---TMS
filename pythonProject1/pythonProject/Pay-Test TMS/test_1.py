import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_web():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://www.google.com/'
    chrome.get(url=url)
    search_box = chrome.find_element(By.CLASS_NAME, 'gLFyf')
    search_box.send_keys('python 3.10')
    search_box.submit()
    assert 'python 3.10' in chrome.title
    time.sleep(10)
   # chrome.close()

