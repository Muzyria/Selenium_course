# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.freeconferencecall.com/ru/ua/login")
time.sleep(1)

check_button = driver.find_element('xpath', '//input[@id="gdpr_checkbox"]')
check_button.click()

el = driver.find_element("xpath", '//button[@id="loginformsubmit"]')
# print(el)
el.click()
# print("-------------------------")
# locator = ("id", "loginformsubmit1")
# el = driver.find_elements(*locator)
# print(el)

time.sleep(3)
