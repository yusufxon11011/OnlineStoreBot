from aiogram.fsm.state import State, StatesGroup


class CategoryStates(StatesGroup):
    newCategory_state = State()

    updCategory_state_list = State()
    updCategory_state_new = State()

    delCategory_state = State()

class ProductStates(StatesGroup):
    newProduct_state = State()

    updProduct_state_list = State()
    updProduct_state_new = State()

    delProduct_state = State()
