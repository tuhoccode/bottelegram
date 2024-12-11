import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True 
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--incognito')         
options.add_argument('--disable-dev-shm-usage')  
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.freeonlinephone.org/receive-sms-online-15085072481.html#read")

time.sleep(5)

rows = driver.find_elements(By.XPATH, "//td[@data-title='Message']")

first_found = False

with open('otp.txt', 'w') as file:
    for row in rows:
        otp_message = row.text.strip()

        otp_match = re.search(r'Your Apple Account Code is: (\d{6})', otp_message)
        
        if otp_match:
            otp = otp_match.group(1)  
            file.write(f"{otp_message} \n{otp}\n")
            first_found = True

driver.quit()
