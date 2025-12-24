from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'), InlineKeyboardButton(text='Контакты', callback_data='contacts')],
    [InlineKeyboardButton(text='Да или Нет', callback_data='random_answer')],
])

async def inline_pins():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Бабочка', url='https://ru.pinterest.com/pin/19492210950124549/'))
    keyboard.add(InlineKeyboardButton(text='Коты в париже', url='https://ru.pinterest.com/pin/11118330333160533/'))
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='back_to_main'))
    return keyboard.adjust(1).as_markup()

async def exit():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='back_to_main'))
    return keyboard.adjust(1).as_markup()