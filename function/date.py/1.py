#Write a Python program to subtract five days from current date
from datetime import datetime , timedelta , date , time
for i in range(5): 
    tomorrow = datetime.now() + timedelta(days=i)
    print(tomorrow)