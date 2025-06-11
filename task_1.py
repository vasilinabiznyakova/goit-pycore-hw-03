from datetime import datetime, timedelta

def get_days_from_today(date):
    today_obj = datetime.today()
    start_day_obj = datetime.strptime(date, "%Y-%m-%d")

    difference = today_obj - start_day_obj

    return difference.days


format_pattern = "%Y-%m-%d"
today_obj = datetime.today()
tomorrow_obj = today_obj + timedelta(days=1)
day_before_yest_obj = today_obj + timedelta(days=-2)


assert get_days_from_today(datetime.strftime(today_obj, format_pattern)) == 0
assert get_days_from_today(datetime.strftime(day_before_yest_obj, format_pattern)) == 2
assert get_days_from_today(datetime.strftime(tomorrow_obj, format_pattern)) == -1
