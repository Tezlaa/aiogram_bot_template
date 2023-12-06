from aiogram import F, Dispatcher, types
from aiogram.filters import CommandStart

from tools.decorators import log_message

from keyboards.inline import button_test


@log_message
async def start(msg: types.Message):
    if not msg.from_user:
        return
    
    await msg.answer("<b>Hello!</b>",
                     reply_markup=button_test.as_markup())


async def button_callback(callback: types.CallbackQuery):
    if not callback.message:
        return
    
    await callback.message.answer(f'Callback data: {callback.data}',
                                  reply_markup=button_test.as_markup())
    

def register_other_handlers(dp: Dispatcher) -> None:
    dp.message.register(start, CommandStart)
    dp.callback_query.register(button_callback,
                               F.text.startswith == button_test.callback_by_button_name('BUTTON'))