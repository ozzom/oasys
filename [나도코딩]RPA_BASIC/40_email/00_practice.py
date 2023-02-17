# import time
# print(time.strftime('%d-%b-%y'))   # %a: 요일(sun, mon, tue....), %b: 월(Jan, Feb, Mar,.... )

import datetime
dt = datetime.datetime.strptime("2021-11-15", "%Y-%m-%d")
# dt.strftime("%d-%b-%Y"))
print('SENTSINCE {}'.format(dt.strftime('%d-%b-%Y')))