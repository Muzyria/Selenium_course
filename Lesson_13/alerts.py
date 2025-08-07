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
wait = WebDriverWait(driver, 30)

BUTTON_ALERT = ("xpath", '//button[@id="alertButton"]')
BUTTON_CONFIRM = ("xpath", '//button[@id="confirmButton"]')
BUTTON_PROMPT = ("xpath", '//button[@id="promtButton"]')



driver.get("https://demoqa.com/alerts")

# wait.until(EC.element_to_be_clickable(BUTTON_ALERT)).click()
# alert = wait.until(EC.alert_is_present())
# driver.switch_to.alert
# time.sleep(3)
# alert.accept()
# time.sleep(3)


# wait.until(EC.element_to_be_clickable(BUTTON_CONFIRM)).click()
# alert = wait.until(EC.alert_is_present())
# driver.switch_to.alert
# time.sleep(3)
# print(alert.text)
# alert.dismiss()
# time.sleep(3)
#
wait.until(EC.element_to_be_clickable(BUTTON_PROMPT)).click()
alert = wait.until(EC.alert_is_present())
# driver.switch_to.alert
time.sleep(3)
alert.send_keys("QWERTY")
alert.accept()
time.sleep(3)
