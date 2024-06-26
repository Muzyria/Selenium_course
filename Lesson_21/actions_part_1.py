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
action = ActionChains(driver)


LEFT_CLICK_BUTTON = ("xpath", "//button[@id='leftClick']")
DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClick']")
RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClick']")
HOVER_BUTTON = ("xpath", "//button[@id='colorChangeOnHover']")

driver.get("https://testkru.com/Elements/Buttons")

left_button = wait.until(EC.visibility_of_element_located(LEFT_CLICK_BUTTON))
double_button = wait.until(EC.visibility_of_element_located(DOUBLE_CLICK_BUTTON))
right_button = wait.until(EC.visibility_of_element_located(RIGHT_CLICK_BUTTON))
hover_button = wait.until(EC.visibility_of_element_located(HOVER_BUTTON))

time.sleep(1)
# action.click(left_button).perform()
# action.double_click(double_button).perform()
# action.context_click(right_button).perform()

# action.click(left_button).pause(1).double_click(double_button).pause(1).context_click(right_button).perform()

action.move_to_element(hover_button).perform()

time.sleep(3)
