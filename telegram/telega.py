import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor
import logging
from aiogram.types import ParseMode
import sqlRequestsTelegram

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6268519128:AAEElauji3zNkJvaRU7LzdKweyYU-4eWQYg")
dp = Dispatcher(bot=bot)

k=0
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message_handler(commands=['opros'])
async def cmd_start(message: types.Message):
    await message.answer("Введите класс")

@dp.message_handler(text="111")
async def echo(message: types.Message):
    global k
    k+=1
    print(k)
    sqlRequestsTelegram.addNewData(message.text,message.text,message.text)
    print(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
