# Chạy Bot trên Windows với Docker

## 1. Cài đặt Docker Desktop

### Bước 1: Tải và cài đặt Docker Desktop
- Truy cập vào trang [tải Docker Desktop](https://www.docker.com/products/docker-desktop).
- Làm theo hướng dẫn để cài đặt Docker cho Windows.
- Sau khi cài đặt xong, mở **Docker Desktop**.

### Bước 2: Đăng nhập vào Docker
- Mở Docker Desktop.
- Đăng nhập vào Docker bằng tài khoản Docker Hub của bạn (nếu chưa có, bạn có thể tạo tài khoản miễn phí tại Docker Hub).

### Bước 3: Mở Terminal trong Docker Desktop
- Trong Docker Desktop, mở **Terminal** (không phải CMD trên Windows).
- Đảm bảo bạn đang sử dụng terminal Docker để thực thi các lệnh Docker.

### Bước 4: Cài đặt WSL (Windows Subsystem for Linux)
  wsl --install

## 2. **Cài đặt xclip**
- sudo apt update
- sudo apt install xclip
- xclip --version

## 3. Chạy docker
- docker pull tuhoccode/botid:real
- docker run -it tuhoccode/botid:real

## 4. Vào telegram
   - Search: afavvbot
   - gõ /id để chạy bot
   - tác dụng: bot tự động lấy tài khoản ilcoud để tải một ứng dụng trả phí(ở đây là shadowrocket)
   - <span style='color:red'>Chú Ý</span>: tài khoản này có thể dùng nhưng không được LOGIN vào CÀI ĐẶT trên iphone(KHÓA MÁY không cứu được), chỉ được login trên APPSTORE(vào mục 'ứng dụng' để tải và đăng xuất ra)
