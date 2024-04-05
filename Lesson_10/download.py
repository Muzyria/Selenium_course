# selenium 4
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": fr"{os.getcwd()}\downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(3)

driver.find_element("xpath", '(//a)[3]').click()

time.sleep(3)
