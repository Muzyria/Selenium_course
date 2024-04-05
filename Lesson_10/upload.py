# selenium 4
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)
driver.find_element("xpath", '//input[@id="file-upload"]').send_keys(fr"{os.getcwd()}\downloads\black-screen.jpg")
time.sleep(5)
