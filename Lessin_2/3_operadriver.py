# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager

webdriver_service = service.Service(OperaDriverManager().install())
webdriver_service.start()

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', True)

driver = webdriver.Remote(webdriver_service.service_url, options=options)