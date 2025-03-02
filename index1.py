from datetime import datetime
def get_days_from_today(date) :
    try :
        date = datetime.strptime(date,"%Y-%m-%d")
        now = datetime.today()
        days_since = now.toordinal() - date.toordinal()
        print(days_since)
    except:
        print("Invalid date format")

get_days_from_today("2025-10-09")
