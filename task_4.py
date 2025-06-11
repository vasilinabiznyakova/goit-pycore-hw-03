from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.06.17"},
    {"name": "Jane Smith", "birthday": "1990.06.24"},
]


def get_upcoming_birthdays(users):
    congratulations_list = []
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        difference = birthday_this_year - today

        if difference.days <= 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            if birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            congratulations_obj = {
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
            }

            congratulations_list.append(congratulations_obj)

    return congratulations_list


upcoming_birthdays = get_upcoming_birthdays(users)
print("List of greetings this week:", upcoming_birthdays)
