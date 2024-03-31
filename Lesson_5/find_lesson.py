# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.freeconferencecall.com/ru/ua/login")

el = driver.find_element("id", "loginformsubmit")
el.click()

time.sleep(3)
