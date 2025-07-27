from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='location', callback_data='location')],
    [InlineKeyboardButton(text='budget', callback_data='budget')],
])
