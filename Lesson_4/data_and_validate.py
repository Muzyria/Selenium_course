# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.wikipedia.org/")

# url = driver.current_url
# print(url)
#
# current_title = driver.title
# print(current_title)
#
# assert url == "https://www.wikipedia.org/", "WRONG URL"
# assert current_title == "Wikipedia", "WRONG TITLE"

print(driver.page_source)

time.sleep(3)

