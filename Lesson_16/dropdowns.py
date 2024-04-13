# selenium 4
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 30)


SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
# DROPDOWN.select_by_visible_text("Option 2")
# DROPDOWN.select_by_value("1")
# DROPDOWN.select_by_index(0)

all_options = DROPDOWN.options

# for option in all_options:
#     time.sleep(1)
#     if "Option 2" in option.text:
#         print("GOOD")
#     DROPDOWN.select_by_visible_text(option.text)

# for option in all_options:
#     time.sleep(1)
#     DROPDOWN.select_by_index(all_options.index(option))

for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))

time.sleep(3)
