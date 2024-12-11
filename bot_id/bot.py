from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Thay token của bạn vào đây
TOKEN = "7866517134:AAEi06H3piW0NmLhHlhiauGPoC-kbFKhNG8"

# Hàm xử lý khi nhận được lệnh /ytb
async def reply_ytb(update: Update, context: CallbackContext) -> None:
    # Gửi tin nhắn "Xin chào ytb" lại cho người dùng
    await update.message.reply_text('Xin chào ytb')

# Hàm xử lý khi nhận được lệnh /id
async def reply_id(update: Update, context: CallbackContext) -> None:
    # Đọc dữ liệu từ file id.txt
    try:
        with open("id.txt", "r") as file:
            lines = file.readlines()
        
        if lines:
            # Gửi ra tài khoản và mật khẩu mới nhất (2 dòng cuối cùng trong file)
            latest_id = lines[-2] if len(lines) >= 2 else "Không có thông tin tài khoản."
            latest_pass = lines[-1] if len(lines) >= 1 else "Không có thông tin mật khẩu."
            response = f"Tài khoản: {latest_id}\nMật khẩu: {latest_pass}"
        else:
            response = "File id.txt không có dữ liệu."
        
        await update.message.reply_text(response)
    except FileNotFoundError:
        await update.message.reply_text("File id.txt không tồn tại.")

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
