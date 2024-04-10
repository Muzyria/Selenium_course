# selenium 4
import os
import time
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 30)

# driver.get("https://www.freeconferencecall.com/ru/ua/login")

# print(driver.get_cookie("country_code"))
# [print(item) for item in driver.get_cookies()]

# driver.add_cookie({
#     "name": "Example",
#     "value": "FIRST_COOKIE"
# })
# print(driver.get_cookie("Example"))


# before = driver.get_cookie("split")
# print(before)
# driver.delete_cookie("split")
# driver.add_cookie({
#     "name": "split",
#     "value": "MY_FIRST_CHANGED_COOKIE"
# })
# print(driver.get_cookie("split"))


# before = driver.get_cookies()
# print(before)
# driver.delete_all_cookies()
# driver.add_cookie({
#     "name": "split",
#     "value": "MY_FIRST_CHANGED_COOKIE"
# })
# print(driver.get_cookies())



# LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")
#
# driver.get("https://www.freeconferencecall.com/en/us/login")
# driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("123")
# driver.find_element(*SUBMIT_BUTTON).click()
# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))


# driver.get("https://www.freeconferencecall.com/en/us/login")
# cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))
#
# driver.delete_all_cookies()
#
# for cookie in cookies:
#     driver.add_cookie(cookie)
#
# driver.refresh()




LOGIN_FIELD = ("xpath", "//input[@placeholder='Login']")
PASSWORD_FIELD = ("xpath", "//input[@placeholder='Password']")
SUBMIT_BUTTON = ("xpath", "//button[@nztype='primary']")

driver.get("https://pressure-dev.hasgas.com.ua/login")
driver.find_element(*LOGIN_FIELD).send_keys("")
driver.find_element(*PASSWORD_FIELD).send_keys("")
driver.find_element(*SUBMIT_BUTTON).click()

print(driver.session_id)

# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

# cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))
# driver.delete_all_cookies()
# for cookie in cookies:
#     driver.add_cookie(cookie)
# print("refresh")
# driver.refresh()


time.sleep(5)

