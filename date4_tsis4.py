from datetime import date, datetime,timedelta,time
a = datetime.today()
b = datetime.strptime("14 February 2023, 07:00:00", "%d %B %Y, %H:%M:%S")
c = (a-b).seconds
print(datetime.today())
print(c)