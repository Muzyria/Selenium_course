# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.freeconferencecall.com/en")

login_button = driver.find_element("xpath", '//a[@id="login-desktop"]')
login_button.click()
time.sleep(3)

email_field = driver.find_element("xpath", '//input[@id="login_email"]')

[print(method) for method in dir(email_field) if not method.startswith('_')]

# email_field.send_keys("123@122.com")
# print(email_field.get_attribute('value'))
# print(email_field.get_attribute('maxlength'))
# time.sleep(2)
# email_field.clear()
# email_field.send_keys('qwerreerytyui')
#
# time.sleep(3)
