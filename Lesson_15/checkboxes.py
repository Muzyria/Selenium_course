# selenium 4
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)


CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")

# driver.get("https://the-internet.herokuapp.com/checkboxes")
#
#
# checkbox_1 = driver.find_element(*CHECKBOX_1)
# print(checkbox_1.is_selected())
# checkbox_1.click()
# print(checkbox_1.is_selected())
#
# assert checkbox_1.get_attribute("checked") is not None
#
# time.sleep(3)


CHECKBOX_HOME = ("xpath", "//span[@class='rct-checkbox']")
CHECKBOX_HOME_STATUS = ("xpath", '//input[@id="tree-node-home"]')

driver.get("https://demoqa.com/checkbox")

checkbox_home = wait.until(EC.element_to_be_clickable(CHECKBOX_HOME))
checkbox_home_status = wait.until(EC.presence_of_element_located(CHECKBOX_HOME_STATUS))
print(checkbox_home_status.is_selected())
checkbox_home.click()
print(checkbox_home_status.is_selected())


time.sleep(5)