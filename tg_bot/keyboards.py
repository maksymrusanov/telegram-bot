from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='location', callback_data='location')],
    [InlineKeyboardButton(text='budget', callback_data='budget')],
])
nav_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='prev page', callback_data='prev'),
     InlineKeyboardButton(text=' finish ', callback_data='finish'),
     InlineKeyboardButton(text='next page ', callback_data='next')],
])
