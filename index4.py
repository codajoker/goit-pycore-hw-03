from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.05"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1992.12.31"}, 
    {"name": "Bob Brown", "birthday": "1988.01.01"}      
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    current_year = today.year
    users_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=current_year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=current_year + 1)

        delta = (birthday_this_year - today).days

        if 0 <= delta <= 7:
            weekday_birthday = birthday_this_year.weekday()
            if weekday_birthday == 5:  
                congragulation_date = birthday_this_year + timedelta(days=2)
            elif weekday_birthday == 6:  
                congragulation_date = birthday_this_year + timedelta(days=1)
            else:
                congragulation_date = birthday_this_year

            users_birthdays.append({
                "name": user["name"],
                "congragulation_date": congragulation_date.strftime("%Y-%m-%d")
            })

    return users_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)