from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет!'
                        f'\nТвой ID: {message.from_user.id}'
                        f'\nИмя: {message.from_user.first_name}',
                        reply_markup=kb.main)


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


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог')
    await callback.message.edit_text('Привет!', reply_markup=await
    kb.inline_cars())
    # await callback.message.answer('Привет!', reply_markup=await
    #                               kb.inline_cars())


@router.message(Command('reg'))
async def get_reg(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя:')


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона:')


@router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Регистрация завершена.'
                         f'\nИмя: {data["name"]}'
                         f'\nНомер: {data["number"]}')
    await state.clear()
