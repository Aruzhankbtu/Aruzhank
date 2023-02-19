#Write a Python program to calculate two date difference in seconds
from datetime import datetime , timedelta , date , time
a = datetime.now()
b = tomorrow = datetime.now() + timedelta(days=1)
print((b-a).total_seconds())