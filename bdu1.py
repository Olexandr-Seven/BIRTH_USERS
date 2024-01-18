from datetime import datetime
import calendar

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
    {"name": "Bruno Adolfovich", "birthday": datetime(1989, 1, 19).date()},
    {"name": "Savva Morozov", "birthday": datetime(1929, 1, 16).date()},
    {"name": "Ivasyk Telesyk", "birthday": datetime(1991, 1, 19).date()},
    {"name": "Svitlana Flower", "birthday": datetime(1982, 10, 16).date()},
    {'name': 'Alex Seven', 'birthday': datetime(1975, 2, 2).date()}
]

def get_birthdays_per_week(users):
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    dict_result = {}

    print(datetime.now().date(), datetime.now().strftime("%A"))

    for ind in users:
        tempo = datetime(year=datetime.now().year, month=ind['birthday'].month, day=ind['birthday'].day)
        string_temp = str(abs(datetime.now().date() - tempo.date()))

        if datetime.now().date() == tempo.date():
            print("Great, ", ind['name'], ' your birthday is TODAY!!! in ', datetime.now().strftime("%A"))
            if tempo.date().strftime("%A") in week_days:
                if tempo.date().strftime("%A") not in dict_result:
                    dict_result[tempo.date().strftime("%A")] = [ind['name']]
                else:
                    dict_result[tempo.date().strftime("%A")].append(ind['name'])

        j = 0
        for i in string_temp:
            if i != ' ':
                j = j + 1
            else:
                break

        if j == 1 and int(string_temp[0:j]) < 7:
            print("Birthday", ind['name'], ' is soon ', 'VERY in ', tempo.strftime("%A"))
            if tempo.strftime("%A") in week_days:
                print(' All right, This day is ', tempo.strftime("%A"))
                if tempo.date().strftime("%A") not in dict_result:
                    dict_result[tempo.date().strftime("%A")] = [ind['name']]
                else:
                    dict_result[tempo.date().strftime("%A")].append(ind['name'])

            elif tempo.strftime("%A") == 'Sunday':
                print("Sunday")
                if week_days[0] not in dict_result:
                    dict_result[week_days[0]] = [ind['name']]
                else:
                    dict_result[week_days[0]].append(ind['name'])
            elif tempo.strftime("%A") == 'Saturday':
                print('Saturday')
                if week_days[0] not in dict_result:
                    dict_result[week_days[0]] = [ind['name']]
                else:
                    dict_result[week_days[0]].append(ind['name'])

    print(dict_result)

get_birthdays_per_week(users)