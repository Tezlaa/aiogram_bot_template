from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("💵Заполнить и отправить резюме"),
    KeyboardButton("🖥Профиль"),
    KeyboardButton("❗Условия и требования")
)