from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Генерация биографии')
        ]
    ],
    resize_keyboard=True
)