# idsh.py
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_account_password():
    options = Options()
    options.headless = True
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--incognito')  
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://vpndata.vn")
    wait = WebDriverWait(driver, 60)

    email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_form_email"]')))
    email.send_keys("tmp4@gmail.com")
    passw = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[2]/div/div/div/div/div/div/input')))
    passw.send_keys("@KH290ba")
    wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[3]/div/div/div/div/div/button'))).click()

    wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))
    time.sleep(5)
    id = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div[3]/div/div/div[2]/div/div[2]/a[7]')))
    id.click()
    tkid = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username_4"]')))
    tkid.click()
    time.sleep(5)  

    def get_clipboard_text():
        try:
            result = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
            return result.stdout.strip()  
        except Exception as e:
            print(f"Không thể truy xuất clipboard: {e}")
            return None

    clipboard_text1 = get_clipboard_text()

    with open("id.txt", "a") as file:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write("user time: " + current_time + "\n")
        file.write(clipboard_text1 + "\n")

    mkid = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password_4"]')))
    mkid.click()
    time.sleep(5)  
    clipboard_text2 = get_clipboard_text()

    with open("id.txt", "a") as file:
        file.write(clipboard_text2 + "\n")

    driver.quit()

    return clipboard_text1, clipboard_text2
