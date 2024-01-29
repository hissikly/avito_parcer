# import telebot
# import requests
# from bs4 import BeautifulSoup
#
#
# bot = telebot.TeleBot('5923786034:AAHMvaXKuY_JXOtDZadhDwiMgRbDacUipW0')
#
#
# @bot.message_handler(commands=['start'])
# def start(mes):
#     bot.send_message(mes.chat.id,
#                      f'<b>Привет,{mes.from_user.first_name}, ты ищешь какой-то товар на авито в Чебоксарах? Я помогу тебе!</b>',
#                      parse_mode='html')
#     bot.send_message(mes.chat.id, f'Чтобы начать поиск пропиши <b>/find<b>', parse_mode='html')
#
#
# @bot.message_handler(commands=['find'])
# def find_product(mes):
#     bot.send_message(mes.chat.id, f'Что хотите найти?')
#     bot.register_next_step_handler(mes, product)
#
#
# def product(mes):
#     source = requests.get('https://www.avito.ru/cheboksary?q=' + mes.text).text
#
#     soup = BeautifulSoup(source, 'html.parser')
#
#     for div in soup.find_all('div', class_='iva-item-body-KLUuy'):
#         url = div.find('div', 'iva-item-titleStep-pdebR').a
#         bot.send_message(url['title'], '\n' + 'https://www.avito.ru' + url['href'])
#         price = div.find('div', 'iva-item-priceStep-uq2CQ').span
#         bot.send_message(price.text, '\n')
#
#
# bot.polling(none_stop=True)
