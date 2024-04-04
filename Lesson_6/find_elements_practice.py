# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://hyperskill.org/tracks")

time.sleep(3)

driver.find_elements("class name", "nav-link")[2].click()

time.sleep(5)

