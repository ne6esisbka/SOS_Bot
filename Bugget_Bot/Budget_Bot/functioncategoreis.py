import os
import datetime
import numexpr as ne

months = datetime.datetime.now().month
years = datetime.datetime.now().year


def get_list(catig):
    if catig == "Products":
        return "Продукты"
    elif catig == "Household":
        return "Хозяйственные товары"
    elif catig == "Apartment":
        return "Квартира"
    elif catig == "Pharmacy":
        return "аптека или врач"
    elif catig == "City":
        return "City"
    elif catig == "Cloth":
        return "Одежда"
    elif catig == "Delivery":
        return "Доставка"
    elif catig == "Transport":
        return "Транспорта"
    elif catig == "Mobile_banks":
        return "Мобильная связь или Банк"
    elif catig == "Hobby":
        return "Хобби"
    elif catig == "Other":
        return "Прочее"
    elif catig == "Traveling":
        return "Путешествие"
    elif catig == "Salary":
        return "Доход"
    elif catig == "Money_box":
        return "Копилка"
    else:
        print("Ошибка в get_list...")

 
# выбор какую категорию расчитать
def select_calculation(calcu):
    dir_date = f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/"
    check_file = f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/{calcu}.txt"
    if os.path.exists(dir_date) and os.path.exists(check_file):
        print(f"Папка существует")

        with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/{calcu}.txt", "r",
                  encoding="UTF-8") as file:
            open_file = file.read()
    elif os.path.exists(dir_date) and not os.path.exists(check_file):
        with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/{calcu}.txt", "a",
                  encoding="UTF-8") as file:
            file.write(f"{get_list(calcu)}:\n0")
    else:
        print("Такой папки нет, сейчас создадим ...")
        if years == dir_date and months == dir_date:
            print(f"Файл существует")
        else:
            os.mkdir(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}")
            for i in calcu:
                with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/{i}.txt", "a",
                          encoding="UTF-8") as file:
                    file.write(f"{get_list(i)}:\n0")
        print(f"файл создан")

    return open_file


# Подсчёт итоговой суммы категории
def sum_of_price_numexpr(prices):
    with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/{prices}.txt", "r",
              encoding="UTF-8") as file:
        read_file = file.read().split("\n")[1]
        res = ne.evaluate(read_file)
    return res


# Подсчёт итоговой суммы категории
def sum_of_price(prices):
    with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/{prices}.txt", "r",
              encoding="UTF-8") as file:
        read_file = file.read().split("\n")
        sum_num = [int(i) for line2 in read_file for i in line2.split("+") if i.isdigit()]
    return sum(sum_num)


# Подсчёт суммы Прочее
def sum_of_other(other):
    with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/{years}_{months}/{other}.txt", "r",
              encoding="UTF-8") as file:
        read_file = file.read().split("\n")
        sum_num = [int(i) for line2 in read_file for i in line2.split(" ") if i.isdigit()]
    return sum(sum_num)


# Подсчёт Копилки
def sum_money_box():
    with open(f"C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Category/Money_Box/Money_box.txt", "r",
              encoding="UTF-8") as file:
        read_file = file.read().split("\n")[1]
        if read_file == "0":
            return 0
        else:
            res = ne.evaluate(read_file)
            return res
