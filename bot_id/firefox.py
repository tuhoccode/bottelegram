from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Khởi tạo Firefox với Selenium
options = Options()
options.headless = False  # Chế độ headless (không giao diện) nếu muốn

# Đường dẫn đến Geckodriver cài đặt qua Snap
service = Service("/snap/bin/geckodriver")

# Khởi tạo trình duyệt Firefox
driver = webdriver.Firefox(service=service, options=options)

# Thực hiện các thao tác trong Selenium
driver.get("https://www.google.com")
