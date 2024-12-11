from telegram.ext import Application
from bot.interactbot import reply_ytb, reply_id 
from telegram.ext import CommandHandler, CallbackContext

TOKEN = "7866517134:AAEe6foII-kyEjPe5tB0AA0e-L9RWa5q0ps"

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("ytb", reply_ytb))

    application.add_handler(CommandHandler("id", reply_id))

    application.run_polling()

if __name__ == '__main__':
    main()
