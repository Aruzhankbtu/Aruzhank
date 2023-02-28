'''
from datetime import date, timedelta
five_days_ago = date.today() - timedelta(5)
print('Today:', date.today())
print('5 days ago:', five_days_ago)
'''
"""
from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print('yesterday:', yesterday)
print('today:', date.today())
print('tomorrow:', tomorrow)
"""
"""
import datetime
datat = datetime.datetime.today().replace(microsecond = 0)
print(datat)
"""
"""
import datetime
d= int(input('Enter hows many days difference:'))
dt1 = datetime.datetime.today().replace(microsecond = 0)
dt2 = dt1 - datetime.timedelta(d)
sum = dt1-dt2
a = sum.total_seconds()
print(f'Difference in seconds: {a}')
"""
'''
import datetime
b = datetime.datetime.now()

print(b)
'''

