#Ex1
from datetime import datetime, timedelta

now_date = datetime.now()

next_date = now_date - timedelta(days = 5)

print("now date:", now_date)
print("next date:", next_date)

#Ex2
from datetime import datetime, timedelta

today_date = datetime.now()

yesterday_date = today_date - timedelta(days = 1)

tomorrow_date = today_date + timedelta(days = 1)

print(today_date)
print(yesterday_date)
print(tomorrow_date)

#Ex3
from datetime import datetime, timedelta

date = datetime.now()

without_microsecond = date.replace(microsecond=0)

print(without_microsecond)

#Ex4
from datetime import datetime, timedelta

date1 = datetime.now()
date2 = date1 - timedelta(days=1)

x = date1 - date2

difference = x.total_seconds()

print(difference)
