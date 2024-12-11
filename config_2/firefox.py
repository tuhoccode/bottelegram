from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False  

service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.google.com")
