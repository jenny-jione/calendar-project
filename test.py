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


    if this_month == 1:
        previous_month = 12
        main_year = input_dt.year - 1
    else:
        main_year = input_dt.year
        previous_month = this_month - 1


    def calculate_week(start_date: datetime, cur_date: datetime):
        monday_cnt = 0
        # input_dt의 week_num
        date = start_date
        delta = timedelta(days=1)
        while date <= cur_date:
            weekday = date.weekday()
            if weekday == 0:
                monday_cnt += 1
            date += delta
        return monday_cnt

    week_num = 0
    if firstday_weekday_num < 4:
        week_num += 1
        prev = False
        week_num += calculate_week(firstday_dt, input_dt)
    else:
        prev = True
        week_num += calculate_week(firstday_dt, input_dt)


    if prev:
        if calculate_week(firstday_dt, input_dt) > 0:
            main_year = input_dt.year
            main_month = input_dt.month
        else:
            if this_month == 1:
                main_year = input_dt.year - 1
                main_month = 12
            else:
                main_year = input_dt.year
                main_month = input_dt.month - 1
    else:
        main_year = input_dt.year
        main_month = input_dt.month
        
    # print(week_num)

    week_num_key = str(week_num) if week_num > 0 else '마지막'

    week_num_dict = {
        '1': '첫째',
        '2': '둘째',
        '3': '셋째',
        '4': '넷째',
        '5': '다섯째',
        '마지막': '마지막'
    }
    week_num_status = week_num_dict[week_num_key]

    # print(input_date)
    week_day_kor = '월화수목금토일'[input_dt.weekday()]
    result = f'{main_year}년 {main_month}월의 {week_num_status}주 {week_day_kor}요일'
    # print(f'{main_year}년 {main_month}월의 {week_num_status}주 {week_day_kor}요일')
    
    print(f'{input_date} ', result)

def get_date_range(start_date, end_date):
    delta = timedelta(days=1)
    result = []
    while start_date <= end_date:
        result.append(start_date)
        start_date += delta
    return result

def main():
    start_date = datetime(2023, 1, 1)
    end_date = datetime.today()
    
    date_range = get_date_range(start_date=start_date, end_date=end_date)
    
    for date in date_range:
        get_weeknum(date)


if __name__ == "__main__":
    main()