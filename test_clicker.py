from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web():
    chrome = webdriver.Chrome()
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    chrome.maximize_window()
    locator_xpath = chrome.find_element(By.XPATH, '//a[contains(@class , "4")]')
    locator_xpath.click()
    locator_css = chrome.find_element(By.CSS_SELECTOR, '([class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]')
    locator_css.click()