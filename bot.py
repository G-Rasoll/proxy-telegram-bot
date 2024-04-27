from telegram import *
from telegram.ext import *
from Database import *
from telegram.constants import *
from uuid import uuid4
from function import *
from telegram.error import *
import datetime, pytz

Updater = Updater("YOUR-TOKEN-BOT")
dis = Updater.dispatcher
j = Updater.job_queue



def start (update,callback:CallbackContext):
    Chat_type = update.message.chat.type
    
    if Chat_type == 'private':
        firstname = update.message.from_user.first_name
        username = update.message.from_user.username
        lastname = update.message.from_user.last_name
        user_id = update.message.from_user.id
        languagecode = update.message.from_user.language_code
        date = tarikh()
        start = CreateUser(firstname,username,lastname,user_id,languagecode,date)

        reply_keyboard = [
            [
                KeyboardButton("دريافت پروکسی")
                ],
                [KeyboardButton("پشتیبانی")],
            
            ]
        update.message.reply_text(("""🔸سلام کاربر گرامی {}  به ربات Telegram Proxy خوش امدید!

🔹برای شروع دکمه (دریافت پروکسی) را فشار دهید.

🔹همچنین برای استفاده اینلاین ادرس ربات را در هر چتی که خواستید تایپ کنید.

{}

🔹راهنمای اعلان ها: با روشن کردن اعلان‌ها ربات به صورت خودکار روزانه یک پروکسی جدید برای شما ارسال خواهد کرد.""").format("<a href='https://t.me/{}'>{}</a>".format(username,firstname),"<code>"+"@Tl_proxybot"+"</code>"),parse_mode=ParseMode.HTML,

            reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True, one_time_keyboard=False)
        )



def Support (update,callback:CallbackContext):
    Chat_type = update.message.chat.type
    if Chat_type == 'private':
        firstname = update.message.from_user.first_name
        username = update.message.from_user.username
        user_id = update.message.from_user.id
        support = Support_bot(firstname,username,user_id)
        reply_keyboard = [[KeyboardButton("برگشت")]]
        update.message.reply_text("""🔹از دريافت انتقادات، نظرات و پیشنهادات شما خرسند می‌شویم.
لطفا پیام خود را ارسال کنید""",
        
            reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True, one_time_keyboard=False)    
        )


def Return (update,callback:CallbackContext):
    Chat_type = update.message.chat.type
    if Chat_type == 'private':
        user_id = update.message.from_user.id
        remove = Return_bot(user_id)
        reply_keyboard = [
            [
                KeyboardButton("دريافت پروکسی")
                ],
                [KeyboardButton("پشتیبانی")],
            
            ]
        update.message.reply_text("""♦️بازگشت به صفحه اصلی""",

            reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True, one_time_keyboard=False)    
        )
        
def send_owner(update,context:CallbackContext):
    chat_type = update.message.chat.type
    if chat_type == "private":
        message = update.message.text

        if message == "دريافت پروکسی":
            request_api = api_proxy()
            keyboard = [
                [
                    InlineKeyboardButton("روشن", callback_data='on'),
                    InlineKeyboardButton("خاموش", callback_data='off'),
                ],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(("{}\n\n🔹دريافت خودکار پروکسی(روزانه)").format(request_api),parse_mode=ParseMode.HTML, reply_markup=reply_markup)



        elif message != "پشتیبانی" and message != "برگشت":
            firstname = update.message.from_user.first_name
            username = update.message.from_user.username
            user_id = update.message.from_user.id
            Search = search_user(user_id)
            if Search == True:
                Updater.bot.send_message(chat_id=297214696,text=("from: {}\nuser_id: {}\nusername: @{}\n\ntext:\n\n{}").format(firstname,user_id,username,message))
                remove = Return_bot(user_id)
                reply_keyboard = [
                    [
                        KeyboardButton("دريافت پروکسی")
                        ],
                        [KeyboardButton("پشتیبانی")],
                    
                    ]
                update.message.reply_text("""🔹پیام شما به تیم پشتیبانی ارسال شد.""",

                    reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True, one_time_keyboard=False)    
                )


def add_daily(update, context: CallbackContext):
    query = update.callback_query
    chat_id = update.callback_query.message.chat_id
    firstname = update.callback_query.from_user.first_name
    username = update.callback_query.from_user.username

    if query.data == 'on':
        add = add_daily_user(firstname,username,chat_id)
        query.message.reply_text("🔹شما به لیست دریافت خودکار پروکسی اضافه شدید.")
    if query.data == 'off':
        delete = delete_daily_user(firstname,username,chat_id)
        query.message.reply_text("♦️شما از لیست دریافت خودکار پروکسی حذف شدید.")



def get_proxy(update,context:CallbackContext):    

    query = update.inline_query.query 
    request_api = api_proxy()
    result = [InlineQueryResultArticle(id = uuid4(),title ='Get proxy1',input_message_content=InputTextMessageContent(request_api,parse_mode=ParseMode.HTML))]
    update.inline_query.answer(result,cache_time=4)
    
def get_proxy_chat(update,context:CallbackContext):
    Chat_type = update.message.chat.type
    if Chat_type == 'private':
        request_api = api_proxy()
        keyboard = [
            [
                InlineKeyboardButton("روشن", callback_data='on'),
                InlineKeyboardButton("خاموش", callback_data='off'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(("{}\n\n🔹دريافت خودکار پروکسی(روزانه)").format(request_api),parse_mode=ParseMode.HTML, reply_markup=reply_markup)

def send_proxy_daily(context:CallbackContext):
    send = search_daily()
    request_api = api_proxy()
    for i in send:
        keyboard = [
            [
                InlineKeyboardButton("روشن", callback_data='on'),
                InlineKeyboardButton("خاموش", callback_data='off'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        Updater.bot.send_message(chat_id = i[3],text = ("{}\n\n🔹دريافت خودکار پروکسي(روزانه)").format(request_api),parse_mode=ParseMode.HTML, reply_markup=reply_markup)




job_minute = j.run_daily(send_proxy_daily,datetime.time(hour=8, minute=0, tzinfo=pytz.timezone('Asia/Tehran')))

print('bot started.....')
dis.add_handler(CommandHandler("start",start))
dis.add_handler(MessageHandler(Filters.regex("پشتیبانی"),Support))
dis.add_handler(MessageHandler(Filters.regex("برگشت"),Return))
dis.add_handler(MessageHandler(Filters.text,send_owner))
dis.add_handler(CallbackQueryHandler(add_daily))
dis.add_handler(InlineQueryHandler(get_proxy))

Updater.start_polling()
Updater.idle()


