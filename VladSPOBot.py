import telebot 
import random 
import logging

from telebot import types 

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("tgbot.log")

bot = telebot.TeleBot("7773810281:AAEMBlyOwEqTnX8GNXV5kEZU83CeFttMW-Q") 

@bot.message_handler(commands=['start']) 
def welcome(message): 
    logger.info(f"Пользователь {message.from_user.first_name} начал взаимодействие с ботом.")
    
    # keyboard 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    item1 = types.KeyboardButton("🎲 Случайное число") 
    item2 = types.KeyboardButton("😊 Как дела?") 

    markup.add(item1, item2) 

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>.".format(message.from_user, bot.get_me()), 
        parse_mode='html', reply_markup=markup)
    logger.info(f"Выведено приветственное сообщение.")

@bot.message_handler(content_types=['text']) 
def chat(message): 
    if message.chat.type == 'private': 
        logger.info(f"Получено сообщение от пользователя {message.from_user.first_name}: {message.text}")
        
        if message.text == '🎲 Случайное число': 
            random_number = random.randint(0, 100)
            bot.send_message(message.chat.id, str(random_number)) 
            logger.info(f"При нажатии на кнопку была произведена отправка сообщения: {random_number}.")
        elif message.text == '😊 Как дела?': 
            markup = types.InlineKeyboardMarkup(row_width=2) 
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good') 
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad') 

            markup.add(item1, item2) 

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup) 
            logger.info(f"Производится отправка сообщения {message.from_user.first_name}: {message.text}")
        else: 
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢') 
            logger.warning(f"Неизвестный запрос от пользователя {message.from_user.first_name}: {message.text}")

@bot.callback_query_handler(func=lambda call: True) 
def callback_inline(call): 
    try: 
        if call.message: 
            if call.data == 'good': 
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊') 
                logger.info(f"Пользователь {call.from_user.first_name} ответил: 'Хорошо'.")
            elif call.data == 'bad': 
                bot.send_message(call.message.chat.id, 'Бывает 😢') 
                logger.info(f"Пользователь {call.from_user.first_name} ответил: 'Не очень'.")

            # remove inline buttons 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?", 
                reply_markup=None) 
            logger.info("Произведено удаление кнопок типа inline.") 

    except Exception as e: 
        logger.error(f"Ошибка при обработке callback: {repr(e)}") 

# RUN 
if __name__ == "__main__":
    logger.info("Бот запущен.")
    bot.polling(none_stop=True)