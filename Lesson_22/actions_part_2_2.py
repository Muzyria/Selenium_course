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


GRID_ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SIDEBAR_ITEM = ("xpath", "(//div[@class='drop-area__item'])[3]")


driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

grid_item = wait.until(EC.presence_of_element_located(GRID_ITEM))
sidebar_item = wait.until(EC.presence_of_element_located(SIDEBAR_ITEM))

time.sleep(1)

action\
    .click_and_hold(grid_item)\
    .pause(2)\
    .move_to_element(sidebar_item)\
    .release()\
    .perform()

time.sleep(3)
