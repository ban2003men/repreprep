from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://github.com/ban2003men/repreprep/')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Site', web_app=web_app)]
    ],
    resize_keyboard=True
)
