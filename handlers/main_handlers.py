from aiogram import types, Dispatcher

from config import admin_id
from loader import bot
from database import DB
from messages import *
from keyboards import *


async def start(message: types.Message):
    DB.add_user(user_id=message.from_user.id, username=message.from_user.username, full_name=message.from_user.full_name)

    logo_img = types.InputFile('database/logo.png')
    await message.answer_photo(photo=logo_img)
    await message.answer(text='👋 Привет! Это бот для заказов Dilikat\nЗдесь вы можете оставить заявку, а наши менеджеры'
                         ' оперативно её обработают.\n\n🔴 Что вас интересует?', reply_markup=main_ikb)

    await message.delete()


async def change_section(callback: types.CallbackQuery):
    if callback.data == 'Главное меню':
        logo_img = types.InputFile('database/logo.png')
        await callback.message.answer_photo(photo=logo_img)
        await callback.message.answer(text='🔴 Вы в главном меню бота. Хотите сделать заказ?', reply_markup=main_ikb)

    if callback.data == 'Материалы':
        await callback.message.answer(text='🔴 Какие расходные материалы интересуют?', reply_markup=materials_ikb)

    if callback.data == 'Оборудование':
        await callback.message.answer(text='🔴 Какое оборудование интересует?', reply_markup=equipment_ikb)

    if callback.data == 'Мои данные':
        customer_info = DB.get_customer(user_id=callback.from_user.id)
        await callback.message.answer(text=await get_customer_info_msg(customer_info),
                                         reply_markup=customer_info_ikb)
    if callback.data == 'Позвонить':
        await callback.message.answer(text='🔴 Наш номер: 88003018733\nНабирайте скорей, мы ждем 😉', reply_markup=call_ikb)

    if callback.data == 'Корзина':
        basket = DB.get_basket(user_id=callback.from_user.id)
        print(basket)
        await callback.message.answer(text=await get_basket_msg(basket), reply_markup=await get_basket_ikb(basket))


async def delete_other_messages(message: types.Message):
    await bot.send_message(chat_id=admin_id, text=f'[ADMIN] Пользователь написал вне сценария: {message.text}\n\n'
                                                  f'id:{message.from_user.id}///{message.from_user.full_name}')
    await message.delete()


def register_main_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(delete_other_messages)

    dp.register_callback_query_handler(callback=change_section, text=['Главное меню', 'Материалы', 'Оборудование',
                                                                      'Мои данные', 'Позвонить', 'Корзина'])
