from aiogram import Bot, Dispatcher, executor, types
import os, re
from databasebot import months, years, start_load_base
from variables import HELP, mounth_read
from replykeyboards import *
from inlinekeyboards import *
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from functioncategoreis import select_calculation, get_list, sum_of_other, sum_money_box, sum_of_price_numexpr


async def on_startup(_):
    print("Семейный дворецкий запущен ...")

# FamilyBudgetBot
storage = MemoryStorage()


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=storage)


# Класс для выбора категории
class FillingStateGroup(StatesGroup):

    category = State()
    number = State()


# команда старт
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет, добро пожаловать, Я Ваш домашний дворецкий!",
                         reply_markup=get_main_menu())
    await message.delete()


# команда хелп
@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message) -> None:
    await message.answer(f"{HELP}")
    await message.delete()


# вывод главного меню
@dp.message_handler(commands=["budget"])
async def cmd_budget(message: types.Message) -> None:
    await message.answer("Выберите действие", reply_markup=get_main_menu())
    await message.delete()


#  вывод клавиатуры выбора категории
@dp.message_handler(Text(equals=["Вести бюджет"]))
async def send_budget(message: types.Message):
    await message.answer(text="Выберите категорию для добавления!",
                         reply_markup=ikb_category_selection)
    await message.delete()
    await message.answer(text=f"Либо выбираем иное ...", reply_markup=closing())
    await FillingStateGroup.category.set()


#  выбор категории
@dp.callback_query_handler(state=FillingStateGroup.category)
async def make_a_categories(callback: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['category'] = callback.data
        if data['category'] == "Other":
            await callback.message.answer(text=f"{select_calculation(data['category'])}\n"
                                               f"Итог = {sum_of_other(data['category'])}")
            await callback.message.answer(text=f"Введите категорию и сумму {get_list(data['category'])}\n"
                                               f"например: море 25000", reply_markup=closing())
        elif data["category"] == "Money_box":
            await callback.message.answer(text=f"{select_calculation(data['category'])}\n"
                                               f"Итог = {sum_money_box()}")
            await callback.message.answer(text=f"Введите сумму {get_list(data['category'])}\n"
                                               f"например:\n 45 или -55 или 25+33-25", reply_markup=closing())
        else:
            await callback.message.answer(text=f"{select_calculation(data['category'])}\n"
                                               f"Итог = {sum_of_price_numexpr(data['category'])}")
            await callback.message.answer(text=f"Введите сумму {get_list(data['category'])}\n"
                                               f"например:\n 45 или -55 или 25+33", reply_markup=closing())
        await FillingStateGroup.next()
        await callback.message.delete()


# действие кнопки отмены
@dp.message_handler(Text(equals=["Отменить"]), state="*")
async def cmd_close(message: types.Message, state: FSMContext) -> None:
    await message.delete()
    await message.answer(text="Ввод окончен, Ваше величество!", reply_markup=ReplyKeyboardRemove())
    await state.finish()


# проверка на число введении суммы
@dp.message_handler(lambda message: not re.search('\d', message.text),
                    state=FillingStateGroup.number)
async def check_number(message: types.Message):
    await message.answer("Вы ввели не правильную сумму")


# введение суммы в категорию
@dp.message_handler(state=FillingStateGroup.number)
async def make_a_number(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['number'] = message.text

    if data['category'] == "Other":
        with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/Other.txt", "a+",
                  encoding="UTF-8") as file:
            file.write(f"{message.text}\n")
        await message.answer(f"Ваша сумма записана!  = {data['number']}", reply_markup=ReplyKeyboardRemove())

    elif data['category'] == "Money_box":
        with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/Money_Box/Money_box.txt",
                  "a+", encoding="UTF-8") as file:
            file.write(f"+{data['number']}")
        await message.answer(f"Ваша сумма записана!  = {data['number']}", reply_markup=ReplyKeyboardRemove())

    else:
        with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/{data['category']}.txt",
                  "a+", encoding="UTF-8") as file:
            file.write(f"+{data['number']}")
        await message.answer(f"Ваша сумма записана!  = {data['number']}", reply_markup=ReplyKeyboardRemove())
    await message.delete()

    await state.finish()


# скинуть EXCEL  файл
@dp.callback_query_handler()
async def load_excel_file(callback: types.CallbackQuery):
    if callback.data == "excel_file":
        await bot.send_document(callback.from_user.id, open("path_to_file.xlsx", "rb"))
    elif callback.data == "excel_file_2":
        await bot.send_document(callback.from_user.id, open("calculations_for_month.xlsx", "rb"))
    await callback.message.delete()


# вывод итогов
@dp.message_handler(Text(equals=["Вывести итоги"]))
async def display_totals(message: types.Message) -> None:
    await message.answer(text=f"{mounth_read()}"
                              f"{start_load_base()}\n"
                              f"Копилка = {sum_money_box()}"
                              f"", reply_markup=ikb_document)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
