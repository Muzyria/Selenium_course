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


LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

driver.get("https://hyperskill.org/login")
wait.until(EC.visibility_of_element_located(LOGIN_FIELD)).send_keys("alekseik@ya.ru")
wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys("Qwerty132!")
wait.until(EC.visibility_of_element_located(SUBMIT_BUTTON)).click()

time.sleep(5)

driver_2 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait_2 = WebDriverWait(driver_2, 30)
driver_2.get("https://hyperskill.org/login")
time.sleep(5)
