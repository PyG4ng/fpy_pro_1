from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


def get_today_date():
    now = datetime.now()
    date_time = now.strftime("%A %d %B %Y")
    print(f"Today's date: {date_time}")


if __name__ == '__main__':
    get_today_date()
    get_employees()
    calculate_salary()
