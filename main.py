from datetime import datetime, timedelta
# input_dt = datetime.today()
input_dt = datetime(2023, 1, 1)
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
    
print(week_num)

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

print(input_date)
week_day_kor = '월화수목금토일'[input_dt.weekday()]
print(f'{main_year}년 {main_month}월의 {week_num_status}주 {week_day_kor}요일')