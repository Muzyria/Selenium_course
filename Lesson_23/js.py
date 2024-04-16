# selenium 4
import time
# JS-код из видео: setTimeout(function() { debugger; }, 5000);

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrolls import Scrolls

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")

driver.get("https://seiyria.com/bootstrap-slider/")


ex_2 = driver.find_element(*EX_2_LOCATOR)

time.sleep(1)
# action.scroll_to_element(ex_2).perform()
# driver.execute_script("arguments[0].scrollIntoView();", ex_2)

scrolls.scroll_to_element(ex_2)

time.sleep(5)
