import logging
from aiogram.types import Message


def log_message(func):
    async def wrapper(*args):

        for arg in args:
            if isinstance(arg, Message):
                msg: Message = arg
                
                if msg.from_user is not None:
                    logging.info(f'| {msg.from_user.id} | @{msg.from_user.username} > "{msg.text}"')

        return await func(*args)
    return wrapper