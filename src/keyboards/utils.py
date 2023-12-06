from typing import List, Optional

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from pydantic import BaseModel


class ButtonType(BaseModel):
    text: str
    callback_data: str


class Button:
    def __init__(self, setup_buttons: List[ButtonType], sizes: tuple = (1, )) -> None:
        """ Create inline button

        Args:
            setup_buttons (List[ButtonType]): settings for InlineKeyboardBuilder,
                Example: [ButtonType(text='text on the button',
                                    callback_data='your_call_back_data'), ...]
            sizes (tuple[int]): buttons to some grid, for example (3, 2) first line will
                                have 3 buttons, the next lines will have 2 buttons

        Returns:
            InlineKeyboardMarkup
        """

        self._setup_buttons = setup_buttons
        
        button = InlineKeyboardBuilder()
        for setup_button in setup_buttons:
            button.add(
                InlineKeyboardButton(
                    text=setup_button.text,
                    callback_data=setup_button.callback_data
                )
            )
        self._button = button.adjust(*sizes)
    
    def as_markup(self):
        return self._button.as_markup()
    
    def callback_by_button_name(self, button_name: str) -> Optional[str]:
        for button in self._setup_buttons:
            if button.text == button_name:
                return button.callback_data