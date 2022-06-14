import telebot
import requests
token = "5074623092:AAEEMwO9XrN_ElW2uoVuQ-19CF_iPsK3nAA"
sudo_user = "h_69053" # يوزرك بدون @
bot = telebot.TeleBot(token)
file = open("admin.txt", 'r')
admin_user = file.readline()
file = open("fcm.txt", 'r')
pr = file.readline()
def id_ls(id):
    result = False
    file = open("users.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

def bk(message):
    bk = open('users.txt', 'rb')
    bot.send_document(message.chat.id, bk)
    
def brod(message):
    mes = message.text
    f = open("users.txt","r")
    for idu in f:
        bot.send_message(idu, text="{}".format(mes))

def brod_fr(message:str):
    mes = message.text
    mei = message.id
    f = open("users.txt","r")
    for idu in f:
        bot.forward_message(idu, str(sudo_id), mei)

def delete_admin(message):
    os.system('rm -fr admin.txt')
    os.system('clear')

def fcm(message):
    mes = message.text
    f = open("fcm.txt", 'a')
    f.write("{}\n".format(mes))
    f.close()
    bot.send_message(message.chat.id, "تم وضع {}@ قناه لشتراك اجباري".format(mes))

def admin_add(message):
    mes = message.text
    f = open("admins.txt", 'a')
    f.write("{}\n".format(mes))
    f.close()
    bot.send_message(message.chat.id, "تم رفع @{} ادمن في البوت بنجاح .".format(mes))
@bot.message_handler(commands=["start"])
def welcome(message):
    idd = message.from_user.id
    if message.chat.type == 'private':
        idu = message.from_user.id
        us = str(message.chat.first_name)
        f = open("users.txt", 'a')
        if(not id_ls(str(idu))):
            f.write("{}\n".format(idu))
            f.close()
    sub = f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@{pr}&user_id={idd}'
    req = requests.get(sub)
    if idd == admin_user or sudo_user or 'member' in req.text or 'creator' in  req.text or 'administrator' in  req.text:
    	pnd = "https://pin.it/7H7FGUy"
    	bot.send_photo(message.chat.id,pnd,"""
- Hi,
- This Bot can help You to Download from YouTube
- Send URL 
- BY - @FZFQBOT""")
    else:
    		bot.send_message(message.chat.id, f'{we} @{pr}')
@bot.message_handler(commands=['mxz'])
def any_msg(message:str):
    if message.from_user.username in sudo_user or admin_user:
        file = open('users.txt', 'r')
        li = len(file.readlines())
        file.close()
        file = open('admin.txt', 'r')
        ad = len(file.readlines())
        file.close()
        admin_keyboard = types.InlineKeyboardMarkup()
        brod = types.InlineKeyboardButton(text='أذاعه .', callback_data='brod')
        del_admin = types.InlineKeyboardButton(text='مسح الادمنيه .', callback_data='delete_all_admin')
        add_admin = types.InlineKeyboardButton(text='اضف ادمن .', callback_data='add_admin')
        brod_fr = types.InlineKeyboardButton(text='أذاعه بلتوجيه .', callback_data='brod_fr')
        bk = types.InlineKeyboardButton(text='نسخه احتياطيه .', callback_data='bk')
        sub = types.InlineKeyboardButton(text=f'عدد المشتركين : {li} .', callback_data='sub')
        admin_list = types.InlineKeyboardButton(text=f'عدد الادمنيه : {ad} .', callback_data='add')
        fc = types.InlineKeyboardButton(text=f'تعيين قناة اشتراك اجباري .', callback_data='fcc')
        admin_keyboard.row_width = 2
        admin_keyboard.add(brod, bk, sub, fc, brod_fr, add_admin, del_admin, admin_list)
        markup_help = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, 'أهلا عزيزي الادمن . \n يمكنك التحكم عن طريق كيبورد اسفل و شكرا .', reply_markup=admin_keyboard)
#----- Start Bot ----- #


#----- Start InLine ----- #
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'brod':
                mesgg = bot.send_message(call.message.chat.id, text='*ارسل لي نص الاذاعه :*', parse_mode='markdown')
                bot.register_next_step_handler(mesgg, brod)

        if call.data == 'brod_fr':
            mesgg = bot.send_message(call.message.chat.id, text='*قم بتوجيه رساله لكي اقوم في اذاعاتها : *', parse_mode='markdown')
            bot.register_next_step_handler(mesgg, brod_fr)

        if call.data == 'bk':
            bk(call.message)

    if call.from_user.username in sudo_user:    
        if call.data == 'fcc':
            mesg = bot.send_message(call.message.chat.id, text='*ارسل يوزر قناة الاشتراك الاجباري :*', parse_mode='markdown')
            bot.register_next_step_handler(mesg, fcm)
    else:
        bot.send_message(call.message.chat.id, "عذرأ الامر يخص المطور الاساسي فقط .")

    if call.from_user.username in sudo_user:  
        if call.data == 'delete_all_admin':
                mesgg = bot.send_message(call.message.chat.id, text='*تم تنزيل جميع الادمنيه بنجاح .*', parse_mode='markdown')
                bot.register_next_step_handler(mesgg, delete_admin)
    else:
        bot.send_message(call.message.chat.id, "عذرأ الامر يخص المطور الاساسي فقط .")

    if call.from_user.username in sudo_user:    
        if call.data == 'add_admin':
                mesgg = bot.send_message(call.message.chat.id, text='*حسنا ارسل لي يوزر الادمن بدون @ :*', parse_mode='markdown')
                bot.register_next_step_handler(mesgg, admin_add)
    else:
        bot.send_message(call.message.chat.id, "عذرأ الامر يخص المطور الاساسي فقط .")
@bot.message_handler(content_types=['text'])    
def photo(message):
    if message.text:
            get = requests.get(f"https://iuytiuyt.000webhostapp.com/tiktok/s.php?url={message.text}").json()
            bot.send_video(message.chat.id,get,caption=f"<strong>- @FZFQBOT .</strong>",parse_mode="html")
bot.infinity_polling()
