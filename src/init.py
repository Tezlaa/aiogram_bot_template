from config.settings import BOT, DP

from handlers import register_all_handlers


async def __on_startup(*args) -> None:
    register_all_handlers(DP)


async def main():
    DP.startup.register(__on_startup)
    await DP.start_polling(BOT)