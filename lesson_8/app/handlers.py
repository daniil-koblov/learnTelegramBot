from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет!'
                        f'\nТвой ID: {message.from_user.id}'
                        f'\nИмя: {message.from_user.first_name}')


@router.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer('Команда /help')


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.message(Command('get_photo'))
async def get_photo_new(message: Message):
    await message.answer_photo(
        photo='https://i.pinimg.com/originals/92/6f/7a/926f7acd3e6ad0e9298fb2a92b7fa2f7.jpg',
        caption='Какая милая куница!')