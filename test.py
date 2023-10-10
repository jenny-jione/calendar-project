from datetime import datetime, timedelta
# input_dt = datetime.today()
input_dt = datetime(2023, 1, 1)

def get_weeknum(input_dt: datetime):
    input_date = input_dt.date()
    this_month = input_dt.month

    # 이번달 1일의 요일 구하기
    firstday_dt = input_dt.replace(day=1)
    firstday = firstday_dt.date()

    # 0: mon, 1: tue, 2: wed, 3: thu, 4: fri, 5: sat, 6: sun
    firstday_weekday_num = firstday.weekday()

    # firstday_weekday_name = firstday.strftime('%A')    # Tuesday
    firstday_weekday_name = firstday.strftime('%a')      # Tue
    
    result = ''
    if firstday_weekday_num < 4:
        result = 'the first week of this month'
    else:
        result = 'the last week of last month'
        # 재귀. 전 달의 1일의 요일 구해서 <4 판별

    
    print(f'{input_date} ', result)

def get_date_range(start_date, end_date):
    delta = timedelta(days=1)
    result = []
    while start_date <= end_date:
        result.append(start_date)
        start_date += delta
    return result

def main():
    start_date = datetime(2022, 12, 1)
    end_date = datetime.today()
    
    date_range = get_date_range(start_date=start_date, end_date=end_date)
    
    for date in date_range:
        get_weeknum(date)


if __name__ == "__main__":
    main()