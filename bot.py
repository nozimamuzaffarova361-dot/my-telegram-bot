import telebot
from telebot import types

TOKEN = "8891723850:AAFxzEDQZbNCKKQF8HHucUSw0DbHFXfJvu4"
bot = telebot.TeleBot(TOKEN)

# Ma'lumotlarni saqlash uchun lug'atlar
foydalanuvchi_jadvallari = {}
foydalanuvchi_vazifalari = {}


@bot.message_handler(commands=["start"])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("Dars jadvalini ko'rish")
  btn2 = types.KeyboardButton("Jadvalni kiritish")
  btn3 = types.KeyboardButton("Uy vazifasini ko'rish")
  btn4 = types.KeyboardButton("Vazifa kiritish")
  btn5 = types.KeyboardButton("AI yordamchi")
  btn6 = types.KeyboardButton("Bugungi reja")

  markup.add(btn1, btn2)
  markup.add(btn3, btn4)
  markup.add(btn5, btn6)

  bot.send_message(
      message.chat.id,
      "Assalomu alaykum! Men AI o'quvchi yordamchisiman.\n"
      "Kerakli bo'limni tanlang:",
      reply_markup=markup,
  )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  user_id = message.chat.id

  if message.text == "Jadvalni kiritish":
    bot.reply_to(message, "Iltimos, dars jadvalingizni yuboring:")
    bot.register_next_step_handler(message, jadvalni_saqlash)

  elif message.text == "Dars jadvalini ko'rish":
    if user_id in foydalanuvchi_jadvallari:
      bot.reply_to(
          message,
          f"Sizning saqlangan jadvalingiz:\n{foydalanuvchi_jadvallari[user_id]}",
      )
    else:
      bot.reply_to(
          message,
          "Siz hali dars jadvalini kiritmagansiz. 'Jadvalni kiritish'"
          " tugmasini bosing.",
      )

  elif message.text == "Vazifa kiritish":
    bot.reply_to(message, "Iltimos, uy vazifalaringizni yuboring:")
    bot.register_next_step_handler(message, vazifani_saqlash)

  elif message.text == "Uy vazifasini ko'rish":
    if user_id in foydalanuvchi_vazifalari:
      bot.reply_to(
          message,
          f"Sizning saqlangan uy vazifalaringiz:\n{foydalanuvchi_vazifalari[user_id]}",
      )
    else:
      bot.reply_to(
          message,
          "Siz hali uy vazifasini kiritmagansiz. 'Vazifa kiritish' tugmasini"
          " bosing.",
      )

  elif message.text == "AI yordamchi":
    bot.reply_to(
        message,
        "Men tayyorman! Menga o'qish yoki darslaringiz bo'yicha istalgan"
        " savolingizni yuboring:",
    )
    bot.register_next_step_handler(message, ai_javob_berish)

  elif message.text == "Bugungi reja":
    bot.reply_to(
        message,
        "Bugungi reja: Darslarni o'z vaqtida bajarish va takrorlash.",
    )

  else:
    bot.reply_to(
        message, "Tushunarsiz buyruq. Iltimos, tugmalardan foydalaning."
    )


def jadvalni_saqlash(message):
  user_id = message.chat.id
  foydalanuvchi_jadvallari[user_id] = message.text
  bot.reply_to(message, "Dars jadvalingiz muvaffaqiyatli saqlandi! ✅")


def vazifani_saqlash(message):
  user_id = message.chat.id
  foydalanuvchi_vazifalari[user_id] = message.text
  bot.reply_to(message, "Uy vazifalaringiz muvaffaqiyatli saqlandi! ✅")


def ai_javobberish(message):
  # Bu yerda AI yordamchi o'quvchining savoliga javob qaytaradi
  savol = message.text
  bot.reply_to(
      message,
      f"AI Yordamchi tahlili:\nSizning '{savol}' degan savolingiz bo'yicha"
      " maslahatim: darslarni reja asosida bo'lib o'qing va har biriga"
      " vaqt ajrating!",
  )


bot.infinity_polling()
