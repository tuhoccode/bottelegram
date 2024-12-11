import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Thiết lập Chrome options
options = Options()
options.headless = True  # Chạy không cửa sổ
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--incognito')           # Mở trình duyệt ở chế độ ẩn danh
options.add_argument('--disable-dev-shm-usage')  # Thêm tùy chọn này để tránh các vấn đề với bộ nhớ
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Mở trang web cần lấy thông tin
driver.get("https://www.freeonlinephone.org/receive-sms-online-15085072481.html#read")

# Chờ trang tải xong (có thể thay đổi thời gian chờ)
time.sleep(5)

# Lọc các dòng thông tin có chứa tin nhắn
rows = driver.find_elements(By.XPATH, "//td[@data-title='Message']")

# Biến flag để kiểm tra khi đã ghi xong dòng đầu tiên
first_found = False

# Mở file để lưu OTP
with open('otp.txt', 'w') as file:
    for row in rows:
        otp_message = row.text.strip()

        # Sử dụng biểu thức chính quy để tìm mã OTP trong tin nhắn
        otp_match = re.search(r'Your Apple Account Code is: (\d{6})', otp_message)
        
        if otp_match:
            otp = otp_match.group(1)  # Lấy mã OTP từ kết quả tìm kiếm
            # Lưu thông báo đầy đủ và mã OTP vào file
            file.write(f"{otp_message} \n{otp}\n")
            # Đánh dấu là đã ghi xong dòng đầu tiên
            first_found = True
            break  # Thoát khỏi vòng lặp sau khi ghi dòng đầu tiên

# Đóng trình duyệt
driver.quit()
