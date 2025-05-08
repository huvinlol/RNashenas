import telebot

# توکن رباتت رو اینجا بذار
bot = telebot.TeleBot("7361429625:AAH5vk9wKaegUtFzodWKvMFPjm3iAFNMQCc")

# آیدی تلگرام خودت رو اینجا بذار (میشه با ربات @userinfobot بگیری)
admin_id = 6620890605

# وقتی کاربر /start میزنه
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, " سلام! پیام ناشناس‌تو بنویس تا بفرستم برای صاحب ربات یعنی حسن.")

# هر پیام متنی دیگه رو بگیره و برات بفرسته
@bot.message_handler(func=lambda m: True)
def forward_to_admin(message):
    bot.send_message(admin_id, f"📨 پیام ناشناس:\n{message.text}")
    bot.reply_to(message, "✅ پیامت فرستاده شد. ناشناس بودی😉")

bot.polling()
