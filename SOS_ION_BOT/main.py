from aiogram import Bot, Dispatcher, executor, types
import json
import string
import os
from variables import *
from aiogram.dispatcher.dispatcher import Text
from botfumc import record_mess
from inlinekeyboard import ikb_cmd_start, ikb_create_account
from replykeyboard import loc_building, main_menu, map_building, menu_map
from aiogram.types import ReplyKeyboardRemove
# ##########################################################################################################


# ##########################################################################################################

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


# ######################################### Уведомление о начале работы ######################################
async def on_startup(_):
    print("Бот запущен...")

# #******************************************* del swear words *********************************************


# удаление матных слов в сообщении
@dp.message_handler(lambda message: {i.lower().translate(str.maketrans('', '', string.punctuation))
                                     for i in message.text.split(" ")}
                    .intersection(set(json.load(open("MAT/cenz.json")))) != set())
async def send_no_mat(message: types.Message):
    await message.answer(text=f"Товарищ, {message.from_user.full_name}, а маты то запрещены!!!")
    await message.delete()
# # ********************************************************************************************************


# ************************************ COMMAND BORT *****************************************************


# Команды старт и help
@dp.message_handler(commands=["start", "help"])
async def cmd_start(message: types.Message):
    if message.text == "/start":
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=open("C:/Users/Admin/Desktop/SOS_ION_BOT/INFO/photo_bota.jpg", "rb"),                # photo is bot   *********************
                             caption=f"Приветствую Вас, {message.from_user.first_name}!!!\nЯ версия бота 0.0.11.")
        await message.answer(text=f"Я обладаю всеми необходимыми Вам знаниями, чтобы "
                                  f"<a href='https://google.com'>Ваш сайт</a> не раздавила Вас своей запутанной и "
                                  f"непонятной на первых порах бюрократией. 😎",
                             disable_web_page_preview=True,
                             parse_mode="HTML",
                             reply_markup=main_menu())
        # photo = "C:/Users/Admin/Desktop/SOS_ION_BOT/INFO/photo_bota.jpg",
        # await message.answer(text=)
    elif message.text == "/help":
        await message.answer(text=f"{HELP}", parse_mode="HTML")

    await message.delete()
# ##########################################################################################################

# ########################  ВЫЗОВ ГЛАВНОГО МЕНЮ  #######################################################


@dp.message_handler(commands=["menu"])
async def cmd_main_menu(message: types.Message):
    await message.answer(text=f"Если что-то нужно, то просто спросите меня. Чем короче запрос, тем точнее я отвечу.",
                         reply_markup=main_menu())
    await message.delete()


# #########################################################################################################


# приветствие бота
@dp.message_handler(lambda message: any(item in message.text.lower() for item in privet))
async def send_privet(message: types.Message):
    await message.answer(f"И Вам,<< {message.from_user.full_name} >>, доброго времени суток!!!!\n"
                         f"Если что-то нужно, то просто спросите меня. Чем короче запрос, тем точнее я отвечу.")


# #########################################  кнопки служебных записок ############################################
# вызов записей
@dp.message_handler(Text(equals=["Служебные записки"]))
async def cmd_main_menu(message: types.Message):
    await message.answer(text=f"Если что-то нужно, то просто спросите меня. Чем короче запрос, тем точнее я отвечу.",
                         reply_markup=ikb_cmd_start)
    await message.delete()


# создание учётной записи
@dp.callback_query_handler(Text(equals="create_account"))
async def create_account(callback: types.CallbackQuery):

    await bot.send_document(chat_id=callback.from_user.id,
                            document=open(f"{your_file.txt}", "rb"),                                          # here is your file
                            caption=f"Для создания учетной записи, необходимо заполнить заявку"
                                    f"и прислать ее на почту - ____@gmail.ru")
    await callback.message.answer(text=f"Обязательно заполнить следующие поля: подразделение, ФИО + дата рождения,"
                                       f"дата заполнения.\n"
                                       f"Поля телефон и помещение - по возможности.\n"
                                       f"<b>Остальные поля не трогать!</b>",
                                  parse_mode="HTML")
# ##########################################################################################################


# создание почты академии
@dp.callback_query_handler(Text(equals=["email_academy"]))
async def create_email_academy(callback: types.CallbackQuery):
    await callback.message.answer(text=f"Вход в почту - (https://google.com/). "
                                       f"Для входа нужно использовать свою учетную запись. "
                                       f"Например ( *****@gmail.com ) "
                                       f"Если нет учетной записи, то нужно ее создать.",
                                  reply_markup=ikb_create_account)
# ##########################################################################################################


# КАС и РАСПИСАНИЕ
@dp.callback_query_handler(Text(equals=["kas_rasp"]))
async def create_kas_rasp(callback: types.CallbackQuery):
    await callback.message.answer(text=f"Для доступа в КАС и (или) Расписание, необходимо заполнить заявку и "
                                       f"прислать ее на почту - ******@gmail.com. По заявке дается только "
                                       f"базовый доступ в КАС. Для доступа у другим модулям и подсистеме "
                                       f"Расписание нужно создать заявку через - https://help_me.gmail.com .")
    await bot.send_document(chat_id=callback.from_user.id,
                            document=open(f"{here is your file}", "rb"))                                               # here is your file 
# ##########################################################################################################


# Directum
@dp.callback_query_handler(Text(equals=["directum"]))
async def create_kas_rasp(callback: types.CallbackQuery):
    await callback.message.answer(text=f"Для получения доступа к Directum, необходимо заполнить заявку "
                                       f"и прислать ее на почту - ******@gmail.com")
    await bot.send_document(chat_id=callback.from_user.id,
                            document=open(f"{here is your file }", "rb"),                                                      # here is your file 
                            caption="Необходимо заполнить поля выделенные синим.")

# ###################################### ГЛАВНОЕ МЕНЮ ##############################################################


# Главное меню
@dp.message_handler(Text(equals=["Назад"]))
async def back_mg(message: types.Message):
    await message.answer(text="Вы вернулись в главное меню", reply_markup=main_menu())
    await message.delete()

# ##################################################################################################################

# ##################################### КОРПУСА АКАДЕМИИ ############################################################


# Центральный кампус
@dp.message_handler(Text(equals=["Центральный кампус"]))
async def central_campus(message: types.Message):
    await bot.send_document(message.from_user.id, document=open(f"{ here is your file }", "rb"),            # here is your file 
                            caption="Центральный кампус")
    await message.delete()


# где какой корпус
@dp.message_handler(Text(equals=["Карта"]))
async def maps_buildings(message: types.Message) -> None:
    await message.answer(text="Выбираем действие", reply_markup=menu_map())
    await message.delete()


@dp.message_handler(Text(equals=["Карта расположения корпусов"]))
async def local_building(message: types.Message) -> None:
    await message.answer(text="Выберите Корпус", reply_markup=loc_building())
    await message.delete()


# LOCAL Corpus
@dp.message_handler(Text(startswith=["Корпус"]))
async def get_local_corpus(message: types.Message) -> None:
    if "Корпус" in message.text:
        if message.text == "Корпус 1":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,                   # your coordinates
                                    longitude=11.22222)
        elif message.text == "Корпус 2":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,
                                    longitude=11.22222)
        elif message.text == "Корпус 3":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,
                                    longitude=11.22222)
        elif message.text == "Корпус 4":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,
                                    longitude=11.22222)
        elif message.text == "Корпус 5":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,
                                    longitude=11.22222)
        elif message.text == "Корпус 6":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,
                                    longitude=11.22222)
        elif message.text == "Корпус 7":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,
                                    longitude=11.22222)
        elif message.text == "Корпус 8":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,
                                    longitude=11.22222)
        elif message.text == "Корпус 9":
            await bot.send_location(chat_id=message.chat.id,
                                    latitude=11.22222,
                                    longitude=11.22222)
    await message.delete()

# ############################################################################


# выбор карты корпуса
@dp.message_handler(Text(equals=["Карта внутри корпусов"]))
async def map_buildings(message: types.Message):
    await message.answer(text="Выберите корпус", reply_markup=map_building())
    await message.delete()


#  Карта корпусов
@dp.message_handler(Text(startswith="Карта"))
async def get_local_corpus(message: types.Message) -> None:
    if "Карта" in message.text:
        if message.text == "Карта 1 корп":
            await message.answer(text="1й корпус")
            await bot.send_document(chat_id=message.chat.id,
                                    document=open(f"{here is your file}", "rb"),                   # here is your file
                                    caption="Первый этаж")
            
        elif message.text == "Карта 2 корп":
            await message.answer(text="2й корпус")
            await bot.send_document(chat_id=message.chat.id,
                                    document=open(f"{here is your file}", "rb"),
                                    caption="Первый этаж")
            
        elif message.text == "Карта 3 корп":
            await message.answer(text="3й корпус")
            await bot.send_document(chat_id=message.chat.id,
                                    document=open(f"{here is your file}", "rb"),
                                    caption="Первый этаж")
            
        # elif message.text == "Корпус 4":

        elif message.text == "Карта 5 корп":
            await message.answer(text="5й корпус")
            await bot.send_document(chat_id=message.chat.id,
                                    document=open(f"{here is your file}", "rb"),
                                    caption="Первый этаж")
            
        else:
            await message.answer(text="Нет такого корпуса...\nПопробуйте выбрать другой корпус, спасибо")
    await message.answer(text="Если что пишите 😉", reply_markup=ReplyKeyboardRemove())
   
    await message.delete()


# ############################################## TEST ######################################################


# test_1
# @dp.message_handler(lambda message: message)
# async def partizan(message: types.Message) -> None:
#     await message.answer(text=f"{TEST_1}")
# ##########################################################################################################


# test_2
@dp.message_handler(Text(equals=["test_2"]))
async def partizan(message: types.Message) -> None:
    await message.answer(text=f"{TEST_2}")
# ##########################################################################################################


# test_3
@dp.message_handler(Text(equals=["test_3"]))
async def partizan(message: types.Message) -> None:
    await message.answer(text=f"{TEST_3}")
# ##########################################################################################################


# test_4
@dp.message_handler(Text(equals=["test_4"]))
async def partizan(message: types.Message) -> None:
    await message.answer(text=f"{TEST_4}")
# ##########################################################################################################


# test_5
@dp.message_handler(Text(equals=["test_5"]))
async def partizan(message: types.Message) -> None:
    await message.answer(text=f"{TEST_5}")
# ##########################################################################################################
# @dp.message_handler()


# Все сообщения
@dp.message_handler()
async def message_all(message: types.Message) -> None:
    if message.text.lower() in application_fill_out:
        await message.answer(text=f"Служебные записки", reply_markup=ikb_cmd_start)
        await message.delete()
    elif len(message.text.lower().split()) == 1 and message.text.lower().split() in TESTIKS:
        await message.answer(text=f"Ещё не добавили ни чего )))")

    elif message.text.lower().split()[0] in questions[0]:
        mess_where = message.text.replace("?", "").lower().split()

        if len(mess_where) == 1 or len(mess_where) == 2 and mess_where[-1] not in [j for i in professions for j in i]:
            await message.answer(text=f"попробуйте иначе задать вопрос \n"
                                      f"Например 1: \n"
                                      f"Где сидят айтишники")

        elif len(mess_where) > 1:
            for word in mess_where[1:]:

                if word in professions[0]:
                    await message.answer(text=f"test 1")
                elif word in professions[1]:
                    await message.answer(text=f"test 2")
                elif word in professions[2]:
                    await message.answer(text=f"test 3")
                elif word in professions[3]:
                    await message.answer(text=f"test 4")
                elif word not in professions:
                    pass
                else:
                    await message.answer(text=f"что то пошло не так")
            await message.delete()
        else:
            await message.answer(text=f"попробуйте иначе задать вопрос \n"
                                      f"Например 2: \n"
                                      f"Где сидят коты?")

    elif message.text.lower().split()[0] in questions[1]:
        mess_how = message.text.replace("?", "").lower().split()

        if len(mess_how) == 1 or len(mess_how) == 2 and mess_how[1:]\
                not in application_fill_out:
            await message.answer(text=f"попробуйте иначе задать вопрос \n"
                                      f"Например : \n"
                                      f"Как написать служебку")

        elif len(mess_how) > 1:
            for word in mess_how[1:]:
                if word in application_fill_out:
                    await message.answer(text=f"Служебные записки", reply_markup=ikb_cmd_start)
                    await message.delete()
                elif word not in application_fill_out and len(mess_how) <= 2:
                    await message.answer(text=f"попробуйте иначе задать вопрос \n"
                                              f"Например : \n"
                                              f"Как написать служебку")
                elif word not in application_fill_out:
                    pass
                else:
                    await message.answer(text=f"попробуйте иначе задать вопрос \n"
                                              f"Например : \n"
                                              f"Как написать служебку")

    else:
        chat = you_chat                                                                      # you chat
        mess_chat = message.chat.id
        user_id = message.from_user.id
        user_name = message.from_user.full_name
        text = message.text
        record_mess(chat, mess_chat, user_id, user_name, text)
        await message.answer(text=f"попробуйте иначе задать вопрос \n"
                                  f"Например : \n"
                                  f"<b>Где сидят айтишники</b> или <b>Как написать служебную записку</b>",
                             parse_mode="HTML")

# ##########################################################################################################

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
