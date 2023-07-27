from functioncategoreis import sum_of_other, sum_of_price_numexpr
import datetime
current_month = datetime.datetime.now().month

HELP = """
здесь команды для помощи

"""

columns_cate = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
                7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

categories_all = ["Products", "Household", "City", "Apartment", "Pharmacy", "Transport", "Mobile_banks",
                  "Delivery", "Hobby", "Other", "Traveling", "Salary", "Cloth"]

print(f"Сегодня {current_month}")


def mounth_read():
    mounth_colection = f"""
{columns_cate[current_month]}
Продукты_________{sum_of_price_numexpr(categories_all[0])}
Хозтовары________{sum_of_price_numexpr(categories_all[1])}
Кв. в City______{sum_of_price_numexpr(categories_all[2])}
Квартира_________{sum_of_price_numexpr(categories_all[3])}
Аптека/Врачи_____{sum_of_price_numexpr(categories_all[4])}
Транспорт________{sum_of_price_numexpr(categories_all[5])}
Моб.связь/Банки___{sum_of_price_numexpr(categories_all[6])}
Доставка_________{sum_of_price_numexpr(categories_all[7])}
Хобби____________{sum_of_price_numexpr(categories_all[8])}
Прочее___________{sum_of_other(categories_all[9])}
Путешествие_______{sum_of_price_numexpr(categories_all[10])}
Одежда___________{sum_of_price_numexpr(categories_all[12])}
Доходы___________{sum_of_price_numexpr(categories_all[11])}
Расходы__________{sum_of_all_categories_result(categories_all)}
"""
    return mounth_colection


# словарь для подсчёта в Базу Данных
def razdel_all(raz):
    sumbol = "/. "
    cate = raz.split('\n')[2:]
    res = [j for i in cate for j in i.split('_') if j.isalpha() or j.isdigit() or j not in sumbol]
    result = {res[i]: res[i + 1] for i in range(0, len(res), 2)}

    return result


# подсчёт суммы за месяц
def sum_of_all_categories_result(categors):
    sum_cat = []
    for i in range(len(categors)):
        if i == 9:
            sum_cat.append(sum_of_other(categories_all[9]))
        elif i == 11:
            pass
        else:
            sum_cat.append(sum_of_price_numexpr(categories_all[i]))

    return sum(sum_cat)


# ############################### переменная для подсчёта за месяц ##########################################
# result_sum_categors = sum_of_all_categors_result(categors_all)  #
# ##############################################################################################################
