from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# ГЛАВНАЯ ПАНЕЛЬ (МЕНЮ)
def main_menu() -> ReplyKeyboardMarkup:
    kb_gm = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_gm.add(KeyboardButton("Карта"), KeyboardButton("Служебные записки"))
    return kb_gm


#  КАРТЫ ГЛАВНОЕ МЕНЮ
def menu_map() -> ReplyKeyboardMarkup:
    kb_mm = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_mm.add(KeyboardButton("Карта расположения корпусов")).add(KeyboardButton("Карта внутри корпусов"))\
        .add(KeyboardButton("Назад"))
    return kb_mm


# расположения корпусов
def loc_building() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    kb.add(KeyboardButton("Корпус 1"), KeyboardButton("Корпус 2"), KeyboardButton("Корпус 3"))\
        .add(KeyboardButton("Корпус 4"), KeyboardButton("Корпус 5"), KeyboardButton("Корпус 6")).\
        add(KeyboardButton("Корпус 7"), KeyboardButton("Корпус 8"), KeyboardButton("Корпус 9"))\
        .add(KeyboardButton("Центральный кампус"), KeyboardButton("Назад"))
    return kb


# карты корпусов
def map_building() -> ReplyKeyboardMarkup:
    kb_mb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_mb.add(KeyboardButton("Карта 1 корп"), KeyboardButton("Карта 2 корп"))\
        .add(KeyboardButton("Карта 3 корп"), KeyboardButton("Карта 5 корп"))\
        .add(KeyboardButton("Назад"))
    return kb_mb
