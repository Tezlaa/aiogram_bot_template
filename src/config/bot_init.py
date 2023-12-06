import os
from typing import Optional

from aiogram import Bot
from aiogram.utils.token import TokenValidationError
from aiogram.enums import ParseMode


class BotInitialization(Bot):
    def __init__(self, parse_mode: str = ParseMode.HTML) -> None:
        BOT_TOKEN = os.getenv('BOT_TOKEN')
        if BOT_TOKEN is None:
            raise TokenValidationError('Set bot token in the .env file!')
        
        super().__init__(BOT_TOKEN, parse_mode=parse_mode)