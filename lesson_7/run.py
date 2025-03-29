import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from api_for_bot import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! \nТвой ID: {message.from_user.id}\nИмя: '
                         f'{message.from_user.first_name}')


@dp.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer('Команда /help')


@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@dp.message(Command('get_photo'))
async def get_photo_new(message: Message):
    await message.answer_photo(
        photo='https://i.pinimg.com/originals/92/6f/7a/926f7acd3e6ad0e9298fb2a92b7fa2f7.jpg',
        caption='Какая милая куница!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
