import asyncio
import logging
import os

from aiogram import Dispatcher, exceptions, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

import createBot
from keyboards.inline import none_age, none_experience, send_resume_question
from keyboards.reply import menu_kb


class FsmSendResume(StatesGroup):
    name = State()
    age = State()
    experience = State()
    finish = State()


async def back_menu(msg: types.Message, state: FSMContext):
    await msg.answer("Главное меню", reply_markup=menu_kb)
    await state.finish()


async def start_resume(msg: types.Message):
    logging.info(f'| {msg.from_user.id} | @{msg.from_user.username} > "{msg.text}"')
    
    await msg.reply("❗Чтобы отправить резюме нам нужно заполнить о Вас информацию",
                    reply_markup=ReplyKeyboardRemove())
    await msg.answer("📋<b>Напишите нам Ваше имя </b>\n<em>'фамилия по желанию'</em>")
    
    await FsmSendResume.name.set()


async def set_name(msg: types.Message, state: FSMContext):
    logging.info(f'| {msg.from_user.id} | @{msg.from_user.username} > "{msg.text}"')
    
    name = msg.text
    async with state.proxy() as data:
        data["name"] = name
    
    await msg.reply(f'👌Отлично, <em>{name}</em>\n📋Теперь отправь свой возраст', reply_markup=none_age)
    
    await FsmSendResume.next()


async def set_age(msg_call: types.Message or types.CallbackQuery, state: FSMContext):
    msg_call = msg_call.message if type(msg_call) is types.CallbackQuery else msg_call
    
    try:
        age = int(msg_call.text)
        if age < 10 or age > 80:
            return await msg_call.reply("❗Отправьте действительный возраст", reply_markup=none_age)
    except Exception:
        age = "-"
    
    async with state.proxy() as data:
        data["age"] = age
    await msg_call.answer("👌Отлично, осталось совсем чуть-чуть")
    await msg_call.answer("📋Есть ли у Вас какой-то опыт в сфере продаж/колл-центров?\n"
                          "<b>📣Коротко расскажите про Ваш опыт\n</b>"
                          " <em>'это может повлиять на скорость нашей обратной связи c Вам'</em>",
                          reply_markup=none_experience)
    
    await FsmSendResume.next()


async def set_experience(msg_call: types.Message or types.CallbackQuery, state: FSMContext):
    if type(msg_call) is types.CallbackQuery:
        msg_call = msg_call.message if type(msg_call) is types.CallbackQuery else msg_call
        experience = "-"
    else:
        await msg_call.reply("👌Отлично!\n<b>Это повлияет на скорость нашей обратной связи</b>")
        experience = msg_call.text
    
    async with state.proxy() as data:
        data["experience"] = experience

    await msg_call.answer("💞Спасибо за предоставление информации!\n"
                          f"📋Имя: {data['name']}\n📋Возраст: {data['age']}\n📋Опыт: {data['experience']}",
                          reply_markup=send_resume_question)
    
    await FsmSendResume.next()


async def finish_state(call: types.CallbackQuery, state: FSMContext):
    logging.info(f'| {call.from_user.id} | @{call.from_user.username} > "{call.data}"')
    
    async with state.proxy() as data:
        pass
    
    callback = (call.data.split("__"))[1]
    if callback == 'send_resume':
        createBot.database.set_info_user(call.from_user.id, data["name"], data['age'], data['experience'])
        await call.message.answer("❗Информация отправлена!\n⏳В ближайшее время с Вами свяжуться", reply_markup=menu_kb)
        await createBot.bot.send_message('331253781', text=createBot.database.get_info_user(call.from_user.id))
        await state.finish()
    else:
        await FsmSendResume.first()
        await call.message.answer("📋Напишите нам Ваше имя <em>фамилия по желанию</em>")
        
    return
    

def register_user_handlers(dp: Dispatcher):
    
    dp.register_message_handler(back_menu, commands=['start'], state=FsmSendResume)
    
    dp.register_message_handler(start_resume, Text(equals='💵Заполнить и отправить резюме'))
    dp.register_message_handler(set_name, state=FsmSendResume.name)
    
    dp.register_callback_query_handler(set_age, text='none_age', state=FsmSendResume.age)
    dp.register_message_handler(set_age, state=FsmSendResume.age)
    
    dp.register_callback_query_handler(set_experience, text='none_experience', state=FsmSendResume.experience)
    dp.register_message_handler(set_experience, state=FsmSendResume.experience)
    
    dp.register_callback_query_handler(finish_state, text_contains=["finish__"], state=FsmSendResume.finish)