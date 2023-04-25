from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web():
    chrome = webdriver.Chrome()
    url = 'https://baraholka.onliner.by/'
    chrome.get(url=url)
    chrome.maximize_window()
    locator_place_an_add = chrome.find_element(By.XPATH, '//strong')
    locator_place_an_add.click()
    locator_video_card_section = chrome.find_element(By.XPATH, '(//ul[@class="b-cm-list"])[2]/li[9]/sup')
    locator_video_card_section.click()
    locator_dress_section = chrome.find_element(By.XPATH, '(//ul[@class="b-cm-list"])[13]/li[5]/sup')
    locator_dress_section.click()