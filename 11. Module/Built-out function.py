# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("Today's date is", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()       # Save today's date
td = datetime.timedelta(days=100)  # Save day = 100
print("우리가 만난 지 100일은", today + td)


