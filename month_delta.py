# timedelta에는 month가 없음.
# => relativedelta를 사용하는 예제
# 시작 날짜부터 지정 날짜까지의 year, month 출력하는 함수
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_year_month_range(start_date: datetime, end_date: datetime):
    delta = relativedelta(months=1)
    end_date = end_date.replace(day=1)
    while (start_date <= end_date):
        print(start_date.year, start_date.month)
        start_date += delta


def main():
    start_date = datetime(2022, 1, 1)
    end_date = datetime.today()
    
    get_year_month_range(start_date, end_date)


if __name__ == "__main__":
    main()