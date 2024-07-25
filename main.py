import asyncio
import logging
import sys
from ORM import User
from qr_code_maker.qr_maker import regular, animated
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
import requests
from aiogram.types import FSInputFile


TOKEN = "6960524676:AAFEpxgsljTliKSczHcOnNFEtv7TldnSLWQ"
dp = Dispatcher()
bot = Bot(TOKEN)


@dp.message(Command("start"))
async def start(message: types.Message):
    await write_data(message)
    await message.answer("Assalomu alaykum!")
    await message.answer("Oddiy QR Code yaratish uchun reg+ma'lumot buyrugini kiriting.")
    await message.answer("Gifli QR Code yaratish uchun ani+ma'lumot buyrugini kiriting.")


@dp.message(F.text.startswith("reg"))
async def regular_maker(message: Message):
    data = message.text
    photo_path = await regular(data[3::])
    photo = FSInputFile(photo_path)
    await message.answer_photo(photo=photo)



@dp.message(F.text.startswith("ani"))
async def animated_maker(message: Message):
    data = message.text
    photo_path = await animated(data[3::])
    gif = FSInputFile(photo_path)
    await message.answer_animation(animation=gif)


async def write_data(message: Message):
    User(message.from_user.first_name,
        message.from_user.last_name,
        message.from_user.username,
        message.from_user.id).insert()


@dp.message()
async def message_sender(message: Message):
    logging.basicConfig(filename='test.log', filemode='a', level=10,
                        format='%(message)s|Time: %(asctime)s')
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Could not send message!")


async def main() -> None:
    global bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
