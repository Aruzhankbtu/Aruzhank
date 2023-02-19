#Write a Python program to drop microseconds from datetime
from datetime import datetime , timedelta , date , time
tim = str(datetime.now())
tim1 = tim.split(".")
print(tim1[0])