from datetime import datetime, timedelta
import time


"""
기준: 2016-12-01 ~ 2023-10-01 총 2496일
date_range length: 2496

함수 설명:
get_weeknum_1: 반복문을 사용하여 firstday와 input_date 사이에 있는 Mon의 개수를 통해 weeknum을 계산
get_weeknum_2: 공식을 만들어 weeknum을 계산

[get_weeknum_1] runtime: 0.012355
[get_weeknum_2] runtime: 0.001047

결론: get_weeknum_1보다 get_weeknum_2의 속도가 10배 이상 빠름.
"""


# 반복문을 사용하여 firstday와 input_date 사이에 있는 M의 개수를 통해 weeknum을 계산하는 함수
def get_weeknum_1(input_date: datetime):
    # 이번달 1일의 요일 구하기
    firstday = input_date.replace(day=1)
    
    # datetime.weekday() 결과 구분 
    # 0: mon, 1: tue, 2: wed, 3: thu, 4: fri, 5: sat, 6: sun
    weeknum = 0
    if firstday.weekday() < 4:
        weeknum += 1
    
    date = input_date.replace(day=1)
    while date <= input_date:
        if date.weekday() == 0:
            weeknum += 1
        delta = timedelta(days=1)
        date += delta

    # print(f'{input_date.date()}\tweeknum: {weeknum}\tweekday: {input_date.strftime("%a")}')


# 공식으로 weeknum을 계산하는 함수
def get_weeknum_2(input_date: datetime):
    firstday = input_date.replace(day=1)
    weeknum = 0
    if firstday.weekday() < 4:
        weeknum += 1
    weeknum += (input_date.day + firstday.weekday() - 1) // 7
    # print(f'{input_date.date()}\tweeknum: {weeknum}\tweekday: {input_date.strftime("%a")}')
    return weeknum


def get_date_range(start_date, end_date):
    delta = timedelta(days=1)
    result = []
    while start_date <= end_date:
        result.append(start_date)
        start_date += delta
    return result


# 실행시간 계산
def chk_runtime(t2: time, t1: time, func_name: str):
    runtime = round(t2-t1, 6)
    print(f'[{func_name}] runtime: {runtime}')


def main():
    start_date = datetime(2016, 12, 1)
    target_date = datetime(2023, 10, 1)
    
    date_range = get_date_range(start_date=start_date, end_date=target_date)
    print(f'date_range length: {len(date_range)}')
    
    t1 = time.time()
    for date in date_range:
        get_weeknum_1(date)
    t2 = time.time()
    chk_runtime(t2, t1, 'get_weeknum_1')
    
    t1 = time.time()
    for date in date_range:
        get_weeknum_2(date)
    t2 = time.time()
    chk_runtime(t2, t1, 'get_weeknum_2')


if __name__ == "__main__":
    main()