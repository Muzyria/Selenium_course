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


LOGIN_FIELD = ("xpath", "//input[@placeholder='Login']")
PASSWORD_FIELD = ("xpath", "//input[@placeholder='Password']")
SUBMIT_BUTTON = ("xpath", "//button[@nztype='primary']")

driver.get("https://pressure-dev.hasgas.com.ua/login")

# driver.find_element(*LOGIN_FIELD).send_keys("")
# driver.find_element(*PASSWORD_FIELD).send_keys("")
# driver.find_element(*SUBMIT_BUTTON).click()
#
# time.sleep(3)

# print(driver.execute_script("return window.sessionStorage.getItem('refresh');"))
# sstorage = driver.execute_script("return sessionStorage;")
# for k, v in sstorage.items():
#     print(k, v)
# pickle.dump(driver.execute_script("return sessionStorage;"), open(os.getcwd() + "/session_storage/sstorage.pkl", "wb"))

sstorage = pickle.load(open(os.getcwd() + "/session_storage/sstorage.pkl", "rb"))

for key, value in sstorage.items():
    driver.execute_script(f"window.sessionStorage.setItem('{key}', '{value}');")

print("refresh")
driver.refresh()


time.sleep(5)

