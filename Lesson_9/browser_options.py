# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
# chrome_options.page_load_strategy = "eager"
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

start_time = time.time()

driver.get("https://beta.syncwise360.com/login")

end_time = time.time()
result = end_time - start_time

print(result)

time.sleep(5)
