from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb_cmd_start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Создание учётной записи",
                          callback_data="create_account")],
    [InlineKeyboardButton("Почта",
                          callback_data="email_academy"),
     InlineKeyboardButton("КАС и расписание",
                          callback_data="kas_rasp")],
    [InlineKeyboardButton("Directum",
                          callback_data="directum")]
])

ikb_create_account = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Создание учётной записи",
                          callback_data="create_account")]
])

# ikb_loc_building = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton("Корпус 1", callback_data="building_1"),
#      InlineKeyboardButton("Корпус 2", callback_data="building_2"),
#      InlineKeyboardButton("Корпус 3", callback_data="building_3")],
#     [InlineKeyboardButton("Корпус 4", callback_data="building_4"),
#      InlineKeyboardButton("Корпус 5", callback_data="building_5"),
#      InlineKeyboardButton("Корпус 6", callback_data="building_6")],
#     [InlineKeyboardButton("Корпус 7", callback_data="building_7"),
#      InlineKeyboardButton("Корпус 8", callback_data="building_8"),
#      InlineKeyboardButton("Корпус 9", callback_data="building_9")]
# ])