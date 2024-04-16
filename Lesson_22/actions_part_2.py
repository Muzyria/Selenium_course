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


ITEM_A = ("xpath", "//div[@id='column-a']")
ITEM_B = ("xpath", "//div[@id='column-b']")

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

item_a = wait.until(EC.presence_of_element_located(ITEM_A))
item_b = wait.until(EC.presence_of_element_located(ITEM_B))

time.sleep(1)
print(item_a.text)
print(item_b.text)
action.drag_and_drop(item_a, item_b).perform()
print(item_a.text)
print(item_b.text)
time.sleep(3)
