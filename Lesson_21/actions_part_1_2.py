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


MAIN_ITEM_2 = ("xpath", "//a[text()='Main Item 2']")
SUB_SUB_LIST = ("xpath", "//a[text()='SUB SUB LIST »']")
SUB_SUB_ITEM_2 = ("xpath", "//a[text()='Sub Sub Item 2']")

driver.get("https://demoqa.com/menu")

main_item_2 = wait.until(EC.presence_of_element_located(MAIN_ITEM_2))
sub_sub_list = wait.until(EC.presence_of_element_located(SUB_SUB_LIST))
sub_sub_item_2 = wait.until(EC.presence_of_element_located(SUB_SUB_ITEM_2))

time.sleep(1)

action.move_to_element(main_item_2).pause(1).move_to_element(sub_sub_list).pause(1).move_to_element(sub_sub_item_2).pause(1).perform()
time.sleep(3)
