# Simple template for Aiogram v.3 using a pattern of registering handlers

1. ### Configuration in `src/config/settings`:
    You can change the database name (currently available only for sqlite):    
    ```python
    DATABASE = {
        'DATABASE_NAME': 'TestDB'
    }
    ```
    Change the storage manager (default is MemoryStorage):
    ```python
    storage = MemoryStorage()
    ```

2. ### Set token from [BotFather](https://t.me/BotFather)
    Rename the `.env.example` file to `.env`
    *Linux:*
    ```bash
    mv .env.example .env
    ```
    Set the token in the file to `BOT_TOKEN = `
    *Example:*
    ```
    BOT_TOKEN = 423432324:fgdfdgPDDnHUBCsUTZRR9KUE-5dfgsPk6E-qldfE
    ```

3. ## Database tables:
    Open the file with the example table `src/models/tables.py`
    \
    To create your own database table, you need to inherit from `models.base.database.Table` and override the abstract method `create_table` where you'll need to create an SQL query to create a table.
    \
    The class `models.base.database.Table` has methods for simple creating SQL queries and committing them: 
    ```python
        self.sql_query_and_commit(sql='your SQL query', variables='your variables')
        # Example:
        self.sql_query_and_commit(
            sql='INSERT INTO table_test (id, mess, user) VALUES(?, ?, ?);',
            variables=(1, 'hello', 'Tezla')
        )
    ```
    \
    It also has a private attribute `_database` with `self.connect` and `self.cursor` attributes for creating your own method for interactions with the database object

4. ## Creating handlers:
    You have a main handler in `src/handlers/main.py` that handles all your handlers. You can add new handlers to the `handlers` tuple to include them in the processing.
    *To register a new handler, import it in the `__init__.py` (check how I do that in the example handlers)*
    
    ###### How to create a new handler?
    In `src/handlers/user/other.py`, you can find a simple example of how you can do that.
    Create an async function following the Aiogram documentation and register it in the `register_other_handlers` *(or another handler of your choice)*

5. ## Buttons:
    You can create a new inline button using my useful class `keyboards.utils.Button`
    This class takes `ButtonType` also from `keyboards.utils.ButtonType` with inline button settings and button size (`adjust()`. You can check the [official documentation](https://docs.aiogram.dev/en/dev-3.x/utils/keyboard.html#usage-example) for an understanding of what it is. Example:
    ```python 
    button_test = Button([
        ButtonType(text="BUTTON", callback_data="CALLBACK_DATA"),
        ButtonType(text="BUTTON1", callback_data="CALLBACK_DATA1"),
        ButtonType(text="BUTTON2", callback_data="CALLBACK_DATA2"),
        ButtonType(text="BUTTON3", callback_data="CALLBACK_DATA3"),
    ], (1, 3))
    ```
    \
    It has a method for `as_markup()` to be sent together with a message in the chat.
    \
    It also has a method for searching callback_data `callback_by_button_name(button_name: str)` for useful handling of button presses, taking only the button_name and returning callback_data or None
