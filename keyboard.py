from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='У меня вопрос!')]
], resize_keyboard=True, input_field_placeholder='Ваш вопрос')
