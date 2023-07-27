from config import db_name, host, user, password
from variables import razdel_all,\
    mounth_read, sum_of_all_categories_result, categories_all, columns_cate
from functioncategoreis import sum_money_box
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

print(f"Текущий месяц : {columns_cate[months]}")


#  запись в базу данных
def start_load_base():
    rachet_categ = razdel_all(mounth_read())
    sum_of_all_categories_result(categories_all)

# запрос к базе данных
    try:
        conn = psycopg2.connect(
            database=db_name,
            host=host,
            user=user,
            password=password
        )
        with conn.cursor() as cursor:
            cursor.execute(
                f"""
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Продукты')}
                WHERE id = {1};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Хозтовары')}
                WHERE id = {2};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Кв. в Коврове')}
                WHERE id = {3};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Квартира')}
                WHERE id = {4};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Аптека/Врачи')}
                WHERE id = {5};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Транспорт')}
                WHERE id = {6};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Моб.связь/Банки')}
                WHERE id = {7};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Доставка')}
                WHERE id = {8};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Прочее')}
                WHERE id = {9};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Хобби')}
                WHERE id = {10};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Путешествие')}
                WHERE id = {11};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Одежда')}
                WHERE id = {12};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {sum_money_box()}
                WHERE id = {13};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {rachet_categ.get('Доходы')}
                WHERE id = {14};
                UPDATE expenses_per_month
                SET {columns_cate[months]} = {sum_of_all_categories_result(categories_all)}
                WHERE id = {15};
    
                SELECT Категория,Январь,Февраль,Март,Апрель,Май, Июнь, Июль, Август, Сентябрь, Октябрь, Ноябрь,Декабрь
                FROM expenses_per_month
                WHERE id < 15
                ORDER BY id;
                
                """
            )
            reading_in_mouth = cursor.fetchall()
            print(f"reading_in_mouth\n{reading_in_mouth}")


        conn.commit()
        conn.close()
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    finally:
        print("Close connect ...")
    print(f"Результат работы функции...")


# показ таблицы расходов в месяц
    df_mounts = pd.DataFrame(data=reading_in_mouth, columns=col_mounts)
    df_mounts.to_excel("path_to_file.xlsx", index=False)
    month_results = df_mounts.head(15)


    with open("C:/Users/Admin/Desktop/Bugget_Bot/Budget_Bot/record.txt", "w+", encoding="UTF-8") as file:
        file.write(f"{month_results}")


#  ####################################################################################################
# файлы для проверки записей в БД
