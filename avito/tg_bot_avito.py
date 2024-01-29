from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import requests
from bs4 import BeautifulSoup

TOKEN = '5923786034:AAHMvaXKuY_JXOtDZadhDwiMgRbDacUipW0'
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/find'))


class StateProduct(StatesGroup):
    product = State()


@dp.message_handler(commands=['start'])
async def get_user_text(mes: types.Message):
    await mes.answer(
        f'<b>Привет,{mes.from_user.first_name}, ты ищешь какой-то товар на авито в Чебоксарах? Я помогу тебе!</b>',
        parse_mode='html')
    await mes.answer(f'Чтобы начать поиск пропиши <b>/find</b>', parse_mode='HTML',  reply_markup=kb)


@dp.message_handler(commands=['find'])
async def get_user_text(mes: types.Message):
    await mes.reply('<b>Погнали!</b>', parse_mode='html')
    await mes.answer('Что ты ищешь?')
    await StateProduct.product.set()


@dp.message_handler(content_types=['text'], state=StateProduct.product)
async def get_state(message: types.Message, state: FSMContext):
    source = requests.get('https://www.avito.ru/cheboksary?q=' + message.text).text
    soup = BeautifulSoup(source, 'html.parser')
    print(soup)
    for div in soup.find_all('div', class_='iva-item-body-KLUuy'):
        url = div.find('div', 'iva-item-titleStep-pdebR').a
        price = div.find('div', 'iva-item-priceStep-uq2CQ').span
        await message.answer(url['title'] + '\n' + 'https://www.avito.ru' + url['href'] + '\n' + price.text)
    await state.finish()


@dp.message_handler()
async def get_user_text(mes: types.Message):
    await mes.answer("Я не совсем понимаю, что ты подразумеваешь под этим...")


if __name__ == '__main__':
    executor.start_polling(dp)
