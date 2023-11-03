import telebot

bot = telebot.TeleBot('6845204526:AAFBGPcHKfhk2CGAGp7CDFzRtBMWuauCGWQ')


@bot.message_handler(commands=['start', 'aboba', 'some'])
def main(mes):
    bot.reply_to(mes, f'halo, {mes.from_user.first_name} {mes.from_user.last_name}')
    bot.send_message(mes.chat.id, '<b>Lets create your account!</b>', parse_mode='html')


@bot.message_handler()
def info(mess):
    if mess.text.lower() == "hi":
        bot.send_message(mess.chat.id, f'halo, {mess.from_user.first_name}')
        bot.send_message(mess.chat.id, 'be more polite even with robot')
    elif mess.text.lower() == 'id':
        bot.send_message(mess.chat.id, f'ID: {mess.from_user.id}')


bot.polling(none_stop=True)