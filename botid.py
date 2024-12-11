import asyncio
import time
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Thay token của bạn vào đây
TOKEN = "7866517134:AAEe6foII-kyEjPe5tB0AA0e-L9RWa5q0ps"

# Hàm xử lý khi nhận được lệnh /ytb
async def reply_ytb(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Xin chào ytb')

# Hàm xử lý khi nhận được lệnh /id
async def reply_id(update: Update, context: CallbackContext) -> None:
    # Chạy Selenium trước khi trả lời
    await update.message.reply_text("Đang lấy tài khoản chờ 30 giây...")
    
    # Tạo và chạy Selenium
    result = await run_selenium()

    # Sau khi Selenium hoàn tất, trả lời người dùng với kết quả
    await update.message.reply_text(result)

# Hàm chạy Selenium
async def run_selenium():
    # Tạo Chrome WebDriver
    options = Options()
    options.headless = True  # Chạy không cửa sổ
    # Tạo Chrome WebDriver
    # options.add_argument('--headless')  # Thay thế headless = True bằng argument
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--incognito')           # Mở trình duyệt ở chế độ ẩn danh
    options.add_argument('--disable-dev-shm-usage')  # Thêm tùy chọn này để tránh các vấn đề với bộ nhớ
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Truy cập vào trang web
    driver.get("https://vpndata.vn")
    wait = WebDriverWait(driver, 60)

    # Đăng nhập và lấy tài khoản, mật khẩu
    email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_form_email"]')))
    email.send_keys("tmp4@gmail.com")
    passw = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[2]/div/div/div/div/div/div/input')))
    passw.send_keys("@KH290ba")
    wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[3]/div/div/div/div/div/button'))).click()
    
    # Truy cập thông tin tài khoản
    wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))
    time.sleep(5)
    id = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div[3]/div/div/div[2]/div/div[2]/a[7]')))
    id.click()
    tkid = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username_4"]')))
    tkid.click()
    time.sleep(5)  # Đợi 5 giây cho trang tải
    def get_clipboard_text():
        try:
            # Sử dụng xclip để lấy nội dung từ clipboard
            result = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
            return result.stdout.strip()  # Lấy nội dung clipboard
        except Exception as e:
            print(f"Không thể truy xuất clipboard: {e}")
            return None

    # Lấy thông tin tài khoản
    clipboard_text1 = get_clipboard_text()


    # Ghi vào file
    with open("id.txt", "a") as file:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write("user time: " + current_time + "\n")
        file.write(clipboard_text1 + "\n")
    
    # Lấy mật khẩu
    mkid = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password_4"]')))
    mkid.click()
    time.sleep(5)  # Đợi 5 giây cho trang tải

    # Cập nhật clipboard và ghi vào file
    clipboard_text2 = get_clipboard_text()

    with open("id.txt", "a") as file:
        file.write(clipboard_text2 + "\n")

    # Đóng trình duyệt
    driver.quit()

    # Trả về kết quả
# Trả về kết quả
    return "Tài khoản: " + clipboard_text1 + "\nMật khẩu: " + clipboard_text2

def main():
    # Khởi tạo bot với token
    application = Application.builder().token(TOKEN).build()

    # Thêm handler để xử lý lệnh /ytb
    application.add_handler(CommandHandler("ytb", reply_ytb))

    # Thêm handler để xử lý lệnh /id
    application.add_handler(CommandHandler("id", reply_id))

    # Bắt đầu bot
    application.run_polling()

if __name__ == '__main__':
    main()
