#Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime , timedelta , date , time
for i in range(-1, 2): 
    days = datetime.now() + timedelta(days=i)
    print(days)