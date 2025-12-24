from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from aiogram.exceptions import TelegramBadRequest

import app.keyboards as kb

import random


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет! \nТвой ID: {message.from_user.id}, \nТвое имя: {message.from_user.first_name}',
                        reply_markup=kb.main)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команада /help')
    

@router.message(F.text =='Как дела?')
async def how_are_you(message: Message):
    await message.answer('Отлично!!!')
    
@router.message(F.text == 'Фото')
async def get_photo(message: Message):
        await message.answer_photo(photo='https://i.pinimg.com/736x/4f/ce/6e/4fce6e0aac4b4fa7cfc5692a65374a7e.jpg', caption='F40')
 
    
@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')
    
    

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог.')
    await callback.message.edit_text('Каталог:', reply_markup=await kb.inline_pins())

@router.callback_query(F.data == 'contacts')
async def contacts(callback: CallbackQuery):
    await callback.answer('Вы выбрали контакты.')
    await callback.message.edit_text("Контакты:" +
                                  "\nТг: @qweqweqwe1v" +
                                  "\nНомер: +79951013116" +
                                  "\nПочта: reflex61@bk.ru",
                                  reply_markup= await kb.exit())

@router.callback_query(F.data == 'basket')
async def contacts(callback: CallbackQuery):
    await callback.answer('Вы выбрали корзину.')
    await callback.message.edit_text('Корзина', reply_markup= await kb.exit())

@router.callback_query(F.data == 'random_answer')
async def random_answer(callback: CallbackQuery):
    answer = random.choice(['Да', 'Нет'])
    await callback.message.edit_text(
        f"Ответ: <b>{answer}</b>", reply_markup=await kb.exit(), parse_mode="HTML"
    )
@router.callback_query(F.data == 'back_to_main')
async def back_to_main(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Главное меню:',
        reply_markup=kb.main
    )