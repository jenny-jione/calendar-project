# 현재 달의 마지막 날짜 구하기
from datetime import datetime, timedelta

def get_lastday():
    input_dt = datetime.today()
    # input_dt = datetime(2023, 12, 31)
    
    if input_dt.month == 12:
        next_month = input_dt.replace(year=input_dt.year + 1, month=1, day=1)
    else:
        next_month = input_dt.replace(month=input_dt.month + 1, day=1)

    lastday_dt = next_month - timedelta(days=1)
    return lastday_dt.date()
    
if __name__ == '__main__':
    result = get_lastday()
    print(result)