

import pyperclip
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = False

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://vpndata.vn")
wait = WebDriverWait(driver, 60)
email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_form_email"]')))
email.send_keys("tmp4@gmail.com")
passw = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[2]/div/div/div/div/div/div/input')))
passw.send_keys("@KH290ba")
wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))
login = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[3]/div/div/div/div/div/button'))).click()
id = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div[3]/div/div/div[2]/div/div[2]/a[7]')))
id.click()
tkid = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username_4"]'))).click()
time.sleep(5)


current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
clipboard_text = pyperclip.paste()
with open("id.txt", "a") as file:
    file.write("user time: " + current_time + "\n")
    file.write(clipboard_text + "\n")  

mkid = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password_4"]'))).click()
time.sleep(5)
with open("id.txt", "a") as file:
    file.write(clipboard_text + "\n")  

print(f"Đã sao chép tk, mk và ghi vào file id.txt: {clipboard_text}")