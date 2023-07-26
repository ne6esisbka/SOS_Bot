import datetime
from variables import questions, professions


date = datetime.datetime.now().date()
time = datetime.datetime.now().time()


def record_mess(chat, mess_chat, user_id, user_name, text):
    if mess_chat == chat:
        with open(f"your file.txt", "a+", encoding="UTF-8")\
                as write_file:
            write_file.write(f"{date} _ {time} -- {user_name} == {text}\n")

    elif mess_chat is not chat:
        with open(f"your {file}.txt", "a+", encoding="UTF-8") as write_file:
            write_file.write(f"{date} _ {time} -- {user_name} == {text}\n")
    else:
        with open(f"your file.txt", "a+", encoding="UTF") as file:
            file.write(f"{date} _ {time} -- {user_name} == {text}\n")


# ############################# ФУНКЦИИ ПОИСКА #############################################################
def check_prof(a):
    any(elem in a for elem in questions[0])
    for word in a.lower().split():
        if word in professions[0]:
            return "test 1"
        elif word in professions[1]:
            return "test 2"
        elif word in professions[2]:
            return "test 3"
        elif word in professions[3]:
            return "test 4"

        elif word not in professions:
            pass
        else:
            return "попробуйте иначе задать вопрос \n" \
                   "Например : \n" \
                   "Где сидят коты?"




# ###################################################################################################################
