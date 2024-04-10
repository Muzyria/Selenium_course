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


LOGIN_FIELD = ("xpath", "//input[@id='username']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@aria-label='submit']")

driver.get("https://beta.syncwise360.com/login")

# driver.find_element(*LOGIN_FIELD).send_keys("QA")
# driver.find_element(*PASSWORD_FIELD).send_keys("")
# driver.find_element(*SUBMIT_BUTTON).click()
# time.sleep(5)
# for i in driver.get_cookies():
#     print(i)
# #
# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))


cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))
driver.delete_all_cookies()

for cookie in cookies:
    print(cookie)
    driver.add_cookie(cookie)

print("refresh")
driver.refresh()


time.sleep(10)
