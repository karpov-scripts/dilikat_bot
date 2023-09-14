from bitrix24 import category_products, product_description
from database import Database

db = Database()

hello_msg = '👋 Привет! Это бот для заказов Dilikat\nЗдесь вы можете оставить заявку, ' \
                'а наши менеджеры оперативно её обработают.\n\n🔴 Что вас интересует?'

main_section_msg = '🔴 Вы в главном меню бота. Хотите сделать заказ?'

materials_section_msg = '🔴 Какие расходные материалы интересуют?'

equipment_section_msg = '🔴 Какое оборудование интересует?'

call_section_msg = '🔴 Наш номер: 88003018733\n' \
                   'Набирайте скорей, мы ждем 😉'


def get_user_info_msg(tg_user_id):
    user_info = db.get_user_info(tg_user_id)
    if user_info:
        user_info_msg = f'🔴 Что мы о вас знаем\n\n' \
                            f'<b>Имя:</b> {user_info[0]} {user_info[1]}\n' \
                            f'<b>Номер телефона:</b> {user_info[2]}\n' \
                            f'<b>Адрес доставки:</b> {user_info[3]}'
    else:
        user_info_msg = '🔴 Мы ничего о вас не знаем!\n\n' \
                            'Запишем информацию, чтобы не спрашивать каждый раз?'
    return user_info_msg


def get_basket_info_msg(tg_user_id):
    basket_info = db.get_user_basket(tg_user_id)
    if basket_info:
        basket_info_msg = '🔴 Ваша корзина\n\n'
        for product in basket_info:
            basket_info_msg += f'<b>Продукт:</b> {product[0]}\n' \
                                   f'<b>Количество:</b>{product[1]}\n\n'
        basket_info_msg += 'Оформляем, или ещё что-то выберите?'

    else:
        basket_info_msg = '🔴 Ваша корзина пуста\n\n' \
                            'Выберете что-нибудь?'
    return basket_info_msg


def get_product_description_msg():
    return product_description


category_products_message = f'🔴 Какой продукт вас интересует?\n\n' \
                            f'{category_products}\n\n' \
                            f'<i> Нажимайте на "id" для перехода к описанию</i>'

change_first_name_msg = f'🔴 Ваше имя?\n\n' \
                        f'<i>Напишите в одном сообщении, пожалуйста</i>'
change_last_name_msg = f'🔴 Ваша фамилия?\n\n' \
                       f'<i>Напишите в одном сообщении, пожалуйста</i>'
change_phone_number_msg = f'🔴 Номер телефона?\n\n' \
                          f'<i>Напишите в одном сообщении, пожалуйста</i>'
change_delivery_address_msg = f'🔴 Ваш адрес для доставки?\n\n' \
                              f'<i>Напишите в одном сообщении, пожалуйста</i>'
