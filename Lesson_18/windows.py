# selenium 4
import time
# JS-код из видео: setTimeout(function() { debugger; }, 5000);

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 30)


FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "(//a[text()=' For Business '])[1]")
START_FREE_BUTTON_LOCATOR = ("xpath", "(//a[text()='Start for Free'])[1]")

driver.get("https://hyperskill.org/tracks")
time.sleep(2)

# print(driver.current_window_handle)
# print(driver.window_handles)
#
# driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
# time.sleep(2)
#
# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])
#
# driver.find_element(*START_FREE_BUTTON_LOCATOR).click()

driver.switch_to.new_window('window')
driver.get("https://hyperskill.org/tracks")


time.sleep(5)
