from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from bot.takeid import get_account_password  

async def reply_ytb(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Xin chào ytb')

async def reply_id(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Đang lấy tài khoản chờ 30 giây...")
    
    account, password = get_account_password()

    await update.message.reply_text(f"Tài khoản: {account}\nMật khẩu: {password}")
