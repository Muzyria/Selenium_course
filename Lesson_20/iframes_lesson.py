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


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)


FORM_NAME_FIELD_LOCATOR = ("xpath", "//input[@id='RESULT_TextField-0']")
COPY_TEXT_BUTTON = ("xpath", "//button[text()='Copy Text']")

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)
driver.switch_to.frame('frame-one796456169')
time.sleep(2)
wait.until(EC.visibility_of_element_located(FORM_NAME_FIELD_LOCATOR)).send_keys("Alex")
time.sleep(2)

driver.switch_to.default_content()

clickable = driver.find_element(*COPY_TEXT_BUTTON)
ActionChains(driver).move_to_element(clickable)
ActionChains(driver).double_click(clickable).perform()

time.sleep(10)

