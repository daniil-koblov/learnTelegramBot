from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню.')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='VK',
                          url='https://vk.com/creator_my_life')]
])

cars = ['Tesla', 'Mercedes', 'BMW', 'Porsche']


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car,
                                          url='https://vk.com/creator_my_life')
                     )
    return keyboard.adjust(2).as_markup(resize_keyboard=True)
