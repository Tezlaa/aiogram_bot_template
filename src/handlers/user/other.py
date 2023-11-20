import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

import createBot
from keyboards.reply import menu_kb


async def start(msg: types.Message):
    logging.info(f'| {msg.from_user.id} | @{msg.from_user.username} > "{msg.text}"')
    
    createBot.database.create_profile(int(msg.from_user.id), f'@{msg.from_user.username}')
    await msg.answer("💵<b>Здравствуйте!</b> Я являюсь ботом для отправки резюме."
                     " <b>Моя задача - помочь вам отправить ваше резюме и контактную "
                     "информацию работодателю для увеличения ваших шансов на получение вакансии.</b>\n"
                     "<em>Выбери интересующее меню снизу⤵</em>",
                     reply_markup=menu_kb)


async def profile(msg: types.Message):
    logging.info(f'| {msg.from_user.id} | @{msg.from_user.username} > "{msg.text}"')

    user_info_db = createBot.database.get_info_user(msg.from_user.id)
    
    result_info = []
    for field in user_info_db:
        if field is None:
            field = "Нет данных"
        elif field == int(msg.from_user.id):
            continue
        
        result_info.append(field)
    
    await msg.answer(f"<b>🖥Профиль</b>\n\nТелеграм: <em>{result_info[0]}</em>\nИмя: <em>{result_info[1]}</em>\n"
                     f"Возраст: <em>{result_info[2]}</em>")


async def feedback(msg: types.Message):
    logging.info(f'| {msg.from_user.id} | @{msg.from_user.username} > "{msg.text}"')

    await msg.answer("<b>🔻Требования к кандидату:</b>\n"
                     "  🔸Грамотная речь\n"
                     "  🔸Желание работать на результат\n"
                     "  🔸Высокая коммуникабельность\n"
                     "  🔸Ответственность и исполнительность\n"
                     "  🔸Стрессоустойчивость\n\n"
                     "<b>🔻Обязанности:</b>\n"
                     "  🔸Выполнение работы на высоком уровне\n"
                     "  🔸Работа с Клиентами\n"
                     "  🔸Сопровождение клиентов\n\n"
                     "<b>🔻Условия работы:</b>\n"
                     "  🔸График работы 9:00-19:00, ПН-ПТ\n"
                     "  🔸Процент от выполненной работы ~200-5000$\n"
                     "  🔸Еженедельные выплаты\n"
                     "  🔸Современный офис с генератором и Starlink\n"
                     "  🔸Обучение и профессиональное развитие\n")
    

def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(profile, Text(equals="🖥Профиль"))
    dp.register_message_handler(feedback, Text(equals="❗Условия и требования"))