# Chạy bot trên Windows với Docker

## Cài đặt Docker Desktop

1. **Tải và cài đặt Docker Desktop**:
   - Truy cập vào trang [tải Docker Desktop](https://www.docker.com/products/docker-desktop).
   - Làm theo hướng dẫn để cài đặt Docker cho Windows.
   - Sau khi cài đặt xong, khởi động Docker Desktop.

2. **Cấu hình Docker**:
     wsl --install

3. **Kiểm tra Docker**:
   - Sau khi cài đặt và cấu hình Docker, mở Command Prompt hoặc PowerShell và kiểm tra Docker:
     ```powershell
     docker --version
     ```
   - Nếu Docker được cài đặt thành công, bạn sẽ thấy phiên bản Docker.

## Chạy Ubuntu container

1. **Tải image Ubuntu**:
   Mở PowerShell hoặc Command Prompt và chạy lệnh sau để tải image Ubuntu từ Docker Hub:
   ```powershell
   docker pull ubuntu
