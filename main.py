import telebot
from config import telebot_token
from exchange_rate import get_exchange_rate
from coinmarket import get_data

bot = telebot.TeleBot(telebot_token)
city = ''


@bot.message_handler(commands=['start'])
def start(message):
    output_message = f"<b>Привет, {message.from_user.first_name} {message.from_user.last_name}!</b>\nВведите город, " \
                     f"в котором вы находитесь, что бы получить данные о курсах валют в вашем районе."
    bot.send_message(message.chat.id, output_message, parse_mode='html')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    input_msg = message.text.strip().lower()
    bot.send_message(message.chat.id, "<i>Пожалуйста, подождите, обрабатываем ваш запрос...</i>", parse_mode='html')
    output_message = get_exchange_rate(input_msg)
    bot.send_message(message.chat.id, output_message, parse_mode='html')
    bot.send_message(message.chat.id, get_data(), parse_mode='html')


if __name__ == '__main__':
    bot.polling(none_stop=True)
