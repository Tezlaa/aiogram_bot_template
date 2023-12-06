from keyboards.utils import Button, ButtonType


button_test = Button([
    ButtonType(text="BUTTON", callback_data="CALLBACK_DATA"),
    ButtonType(text="BUTTON1", callback_data="CALLBACK_DATA1"),
    ButtonType(text="BUTTON2", callback_data="CALLBACK_DATA2"),
    ButtonType(text="BUTTON3", callback_data="CALLBACK_DATA3"),
], (1, 3))