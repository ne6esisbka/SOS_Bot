from config import db_name, host, user, password
from variables import rachet_categ
import psycopg2
import datetime
import pandas as pd

months = datetime.datetime.now().month
years = datetime.datetime.now().year

# таблица за месяц
col_mounts = ["Категория", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь",
              "Октябрь", "Ноябрь", "Декабрь"]
# таблица за год
col_years = ["Название месяца", "Расход", "Приход", "Разница"]

columns_cate_all = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
                    7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

categors_all2 = ["Products", "Household", "Kovrov", "Apartment", "Pharmacy", "Transport", "Mobile_banks", "Delivery",
                 "Hobby", "Other", "Traveling", "Salary"]

print(f"Текущий месяц : {columns_cate_all[months]}")


#  запись в базу данных
def start_load_base():
    # запрос к базе данных
    try:
        conn = psycopg2.connect(
            database=db_name,
            port=5432,
            host=host,
            user=user,
            password=password
        )
        with conn.cursor() as cursor:
            cursor.execute(
                f"""
                UPDATE test
                SET  price = {rachet_categ.get('Продукты')}
                WHERE name = 'Продукты';
                UPDATE test
                SET price = {rachet_categ.get('Хозтовары')}
                WHERE name = 'Хозтовары';
                UPDATE test
                SET price =  {rachet_categ.get('Кв. в Коврове')}
                WHERE name = 'Кв. в Коврове';
                UPDATE test
                SET price =  {rachet_categ.get('Квартира')}
                WHERE name = 'Квартира';
                UPDATE test
                SET price =  {rachet_categ.get('Аптека/Врачи')}
                WHERE name = 'Аптека/Врачи';
                UPDATE test
                SET price =  {rachet_categ.get('Транспорт')}
                WHERE name = 'Транспорт';
                UPDATE test
                SET price =  {rachet_categ.get('Моб.связь/Банки')}
                WHERE name = 'Моб.связь/Банки';
                UPDATE test
                SET price = {rachet_categ.get('Доставка')}
                WHERE name = 'Доставка';
                UPDATE test
                SET price =  {rachet_categ.get('Прочее')}
                WHERE name = 'Прочее';
                UPDATE test
                SET price =  {rachet_categ.get('Хобби')}
                WHERE name = 'Хобби';
                UPDATE test
                SET price =  {rachet_categ.get('Путешествие')}
                WHERE name = 'Путешествие';
                UPDATE test
                SET price =  {rachet_categ.get('Доходы')}
                WHERE name = 'Доходы';

                SELECT Категория,Январь,Февраль,Март,Апрель,Май, Июнь, Июль, Август, Сентябрь, Октябрь, Ноябрь,Декабрь
                FROM expenses_per_month
                WHERE id < 15
                ORDER BY id;

                """
            )

            reading_in_mouth = cursor.fetchall()
            print(f"reading_in_mouth\n"
                  f"{reading_in_mouth}")
        with conn.cursor() as cursor:
            cursor.execute(
                f"""
                UPDATE list_mounths
                SET "Расход" = 23
                WHERE id = 6;

                SELECT Название_месяца, Расход, Приход, Разница FROM list_mounths
                WHERE id < 14;

                """
            )
            reading_of_calculations_for_month = cursor.fetchall()
            print(f"записалось  22222 ...\n{reading_of_calculations_for_month}")

        conn.commit()
        conn.close()
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    finally:
        print("Close connect ...")

    # print(f"Результат работы функции...\n{reading_in_mouth}")

    # # показ таблицы расходов в месяц
    # df_mounts = pd.DataFrame(data=reading_in_mouth[0], columns=col_mounts)
    # df_mounts.to_excel("path_to_file.xlsx", index=False)
    # month_results = df_mounts.head(15)
    #
    # df_years = pd.DataFrame(data=reading_in_mouth[1], columns=col_years)
    # df_years.to_excel("calculations_for_month.xlsx", index=False)
    # years_result = df_years.head(14)
    #
    # with open("C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/record.txt", "w", encoding="UTF-8") as file:
    #     file.write(f"{month_results}")
    #
    # with open("C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/Products.txt", "w", encoding="UTF-8") as file:
    #     file.write(f"{years_result}")
    # result_working_base = [month_results, years_result]
    # print(f"result_working_base\n{result_working_base}")
    # print(f"rachet_categ\n{rachet_categ.get('Моб.связь/Банки')}")
    # print(f"Записалось ...\n{reading_in_mouth}")
    # print(f"записалось  22222 ...\n{reading_of_calculations_for_month}")



#  ####################################################################################################
# файлы для проверки записей в БД
print(start_load_base())
