from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


none_age = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Предпочитаю не указывать", callback_data='none_age'),
)

none_experience = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Не имею опыта", callback_data='none_experience'),
)

send_resume_question = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Всё верно отправить данные", callback_data='finish__send_resume'),
    InlineKeyboardButton(text="Заполнить заново", callback_data='finish__fill_in_again'),
)