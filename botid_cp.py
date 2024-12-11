import time
import subprocess
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext,CallbackQueryHandler, ConversationHandler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


TOKEN = "7866517134:AAEe6foII-kyEjPe5tB0AA0e-L9RWa5q0ps"

async def reply_start(update:Update, context:CallbackContext):
    await update.message.reply_text("Chào mừng bạn đến với bot của Đức Anh!!!")
    await asyncio.sleep(2)
    keyboard = [
        [InlineKeyboardButton("ytb premium (free)", callback_data='ytb')],
        [InlineKeyboardButton("spotify premium (free)", callback_data='spotify')],
        [InlineKeyboardButton("locket gold vĩnh viễn? (trả phí)", callback_data='locket')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bạn muốn lấy...(lưu ý, app free chỉ được lựa chọn 1 lần, hãy suy nghĩ trước khi chọn!)\n", reply_markup=reply_markup)

async def button_handler(update:Update, context:CallbackContext):

    query = update.callback_query
    await query.answer()
    if query.data == 'ytb':
        await reply_ytb(query, context)
    elif query.data == 'spotify':
        await reply_spotify(query, context)
    elif query.data == 'locket':
        await reply_locketgold(query, context)


async def reply_ytb(query:Update, context:CallbackContext):
    await query.message.reply_text("Bạn đã chọn YTB Premium (Free)")
async def reply_spotify(query:Update, context:CallbackContext):
    await query.message.reply_text("Bạn đã chọn Spotify Premium (Free)")
async def reply_locketgold(query:Update, context:CallbackContext):
    await query.message.reply_text("Bạn đã chọn Locket Gold Vĩnh Viễn (Trả phí)")

async def reply_id(update : Update, context: CallbackContext):
    await update.message.reply_text("Đag lấy tài khỏan chờ 30 giây đi ní...")
    result = await selenium()
    await update.message.reply_text(result)



async def selenium():
    options = Options()
    options.headless = True
    options.add_argument('--disable-gpu')
    options.add_argument('incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-ssh')
    options.add_argument('--disable-dev-shm-usage')  
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service = service, options=options)
    driver.get("https://vpndata.vn")
    wait = WebDriverWait(driver,60)

 
    try:
        wait.until(EC.invisibility_of_element_located((By.ID, 'preloader')))
        login_account = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_form_email"]'))).send_keys("tmp4@gmail.com")
        login_password = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[2]/div/div/div/div/div/div/input')))
        login_password.send_keys("@KH290ba")
        wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[3]/div/div/div/div/div/button'))).click()
        try:
            login_error = driver.find_element((By.XPATH, '/html/body/div[3]/div/div'))
            if login_error.is_displayed():
                return "thao tác lại"
            else:
                return None
        except:
            pass

                
        wait.until(EC.invisibility_of_element_located((By.ID, "preloader")))
        time.sleep(5)
        login_idshadow = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div[3]/div/div/div[2]/div/div[2]/a[7]'))).click()
        time.sleep(3)
        copy_account = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username_4"]'))).click()

        def take_id():
            try:
                result_copy = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
                return result_copy.stdout.strip()
            except:
                print(f'có lỗi trong quá trình copy id')
                return None
            
        account_copyed = take_id()
        with open("id.txt" , "a") as file:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            file.writelines(current_time)
            file.writelines(account_copyed)

        time.sleep(3)
        copy_password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password_4"]'))).click()
        password_copyed = take_id()
        with open("id.txt" ,"a") as file:
            file.writelines(password_copyed)

        return "Tài khoản: " + account_copyed + "\nMật khẩu: " + password_copyed
        

    except:
        driver.quit()
        return f'Server đang bảo trì, quay lại sau thời gian ngắn!'
    finally:
        driver.quit()

def main():
    application = Application.builder().token(TOKEN).build()
    #khoi tao nut start
    conv_handler = ConversationHandler(
        entry_points= [CommandHandler('start', reply_start)],
        states= {},
        fallbacks= []
    )
    application.add_handler(CommandHandler('id', reply_id))
    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(button_handler))


    application.run_polling()
if __name__ == '__main__':
    main()