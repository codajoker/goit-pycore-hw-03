from datetime import datetime
from datetime import timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.05"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays (users):
    today = datetime.today().date()
    current_year = today.year
    users_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=current_year)
        weekday_birthday = birthday_this_year.weekday()
        congragulation_date = birthday_this_year
        if (birthday_this_year < today) :             
            print("next year")
            continue
        if (weekday_birthday == 6 ) :
            congragulation_date = birthday_this_year + timedelta(days=1)
        elif (weekday_birthday == 5 ) :
            congragulation_date = birthday_this_year + timedelta(days=2)
        users_birthdays.append({"name": user["name"],  "congragulation_date": congragulation_date.strftime("%Y-%m-%d")})
    return users_birthdays
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
