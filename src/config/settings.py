from dotenv import load_dotenv

from config.bot_init import BotInitialization

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


load_dotenv()


DATABASE = {
    'DATABASE_NAME': 'TestDB'
}


BOT = BotInitialization()

# Can set needed storage manager
storage = MemoryStorage()

DP = Dispatcher(storage=storage)