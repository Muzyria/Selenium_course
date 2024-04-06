# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)

# VISIBLE_AFTER_BUTTON = ('xpath', '//button[@id="visibleAfter"]')
# ENABLE_IN_SECONDS_BUTTON = ('xpath', '//button[@id="enableAfter"]')
#
# driver.get("https://demoqa.com/dynamic-properties")
#
# enable_after = wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS_BUTTON))
# enable_after.click()
#
# visible_after = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))
# visible_after.click()
#
# time.sleep(3)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# REMOVE_BUTTON = ('xpath', "//button[text()='Remove']")
#
# driver.find_element(*REMOVE_BUTTON).click()
# wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
# print("ALL OK")


ENABLE_BUTTON = ('xpath', "//button[text()='Enable']")
TEXT_FIELD = ('xpath', "//input[@type='text']")

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("1234569789")
print(driver.find_element(*TEXT_FIELD).get_attribute("value"))
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "1234569789"))
wait.until(EC.text_to_be_present_in_element_attribute(TEXT_FIELD, "value", "1234569789"))
print("ALL OK")
time.sleep(5)
