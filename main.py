from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    data_now = datetime.now().date()
    print(data_now)
    get_employees()
    calculate_salary()

if __name__ == '__main__':
    main()