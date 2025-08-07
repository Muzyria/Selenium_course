# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


[print(method) for method in dir(driver) if not method.startswith('_')]

# driver.maximize_window()
# driver.get("https://beta2.syncwise360.com/login")
# time.sleep(10)



