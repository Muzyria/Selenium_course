# selenium 4
import time
# JS-код из видео: setTimeout(function() { debugger; }, 5000);

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# http://free-proxy.cz/ru/
PROXI_SERVER = "35.185.196.38:3128"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXI_SERVER}")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 30)

# 194.44.22.37
driver.get("https://stepik.org/")


time.sleep(10)
