from aiogram import types, Dispatcher

from database import DB
from messages import get_category_products_msgs, get_product_msg
from keyboards import get_category_products_ikb, get_product_ikb


async def show_category_products(callback: types.CallbackQuery):
    all_products = await DB.get_products()
    category_name = callback.data
    category_type = [p[9] for p in all_products if p[8] == category_name][0]

    # HERE MAY BE A LOT OF MESSAGES, DEPENDS ON PRODUCTS QUANTITY
    category_products_msgs = get_category_products_msgs(category_name, all_products)

    for i in range(len(category_products_msgs)):
        msg = category_products_msgs[i]
        if msg == category_products_msgs[-1]:
            await callback.message.answer(text=msg, reply_markup=get_category_products_ikb(category_type))
        else:
            await callback.message.answer(text=msg)


async def show_product(message: types.Message):
    product_id = int(message.text.replace('/show_id', ''))
    product = await DB.get_product(product_id)

    product_image_name = product[3]
    product_category_name = product[8]

    product_image = types.InputFile(f'database/catalog/data/product_images/{product_image_name}')
    await message.answer_photo(photo=product_image)
    await message.answer(text=get_product_msg(product),
                         reply_markup=get_product_ikb(product_category_name, product_id),
                         disable_web_page_preview=True)
    await message.delete()


def register_product_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(callback=show_category_products,
                                       text=['3D принтеры', '3D сканеры', 'Фрезерные станки', 'Печи',
                                             'CAD CAM блоки', 'Фрезы', 'Фотополимеры'])

    dp.register_message_handler(callback=show_product, text_startswith=['/show_id'])
