# from datetime import datetime
#
# import pandas as pd
#
# filename = "C:/Users/Admin/PycharmProjects/TestsPythonTest/Budget_Bot/record.txt"
# dt = datetime.now().date().year
#
# products = 0
# apartment = 0
# household = 0
# pharmacy = 0
# kovrov = 0
# transport = 0
# mobile = 0
# banks = 0
# delivery = 0
# other = 0
#
#
# col = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
#        "Ноябрь", "Декабрь", "Год"]
#
# row = ["Продукты", "Квартира", "Хозтовары", "Аптека/Врачи", "Ковров", "Транспорт", "Мобильная связь", "Банки",
#        "Доставка", "Прочее"]
#
#
# new_data = pd.DataFrame(columns=col, index=row, dtype=int)
# pd.set_option("display.max_columns", None)
#
# new_data["Год"] = dt
#
#
# def read_file():
#     global products, apartment, household, pharmacy, kovrov, transport, mobile, banks, delivery, other
#     may = new_data["Май"]
#     with open("C:/Users/Admin/PycharmProjects/TestsPythonTest/Budget_Bot/record.txt", "r", encoding="UTF-8") as file:
#
#         for line in file:
#
#             if "Products" in line:
#
#                 splitted_line = line.split(' ')[2]
#                 products += int(splitted_line)
#                 new_data.at[row[0],  "Май"] = products
#
#             elif "Apartment" in line:
#                 splitted_line = line.split(' ')[2]
#                 apartment += int(splitted_line)
#                 new_data.at[row[1],  "Май"] = apartment
#
#             elif "Household" in line:
#                 splitted_line = line.split(' ')[2]
#                 household += int(splitted_line)
#                 new_data.at[row[2], "Май"] = household
#
#             elif "Pharmacy" in line:
#                 splitted_line = line.split(' ')[2]
#                 pharmacy += int(splitted_line)
#                 new_data.at[row[3], "Май"] = pharmacy
#
#             elif "Kovrov" in line:
#                 splitted_line = line.split(' ')[2]
#                 kovrov += int(splitted_line)
#                 new_data.at[row[4], "Май"] = kovrov
#
#             elif "Transport" in line:
#                 splitted_line = line.split(' ')[2]
#                 transport += int(splitted_line)
#                 new_data.at[row[5], "Май"] = transport
#
#             elif "Mobile" in line:
#                 splitted_line = line.split(' ')[2]
#                 mobile += int(splitted_line)
#                 new_data.at[row[6], "Май"] = mobile
#
#             elif "Banks" in line:
#                 splitted_line = line.split(' ')[2]
#                 banks += int(splitted_line)
#                 new_data.at[row[7], "Май"] = banks
#
#             elif "Delivery" in line:
#                 splitted_line = line.split(' ')[2]
#
#                 delivery += int(splitted_line)
#                 new_data.at[row[8], "Май"] = delivery
#
#             elif "Other" in line:
#                 splitted_line = line.split(' ')[2]
#                 other += int(splitted_line)
#                 new_data.at[row[9], "Май"] = other
#
#             else:
#                 return may
#
#     return may
