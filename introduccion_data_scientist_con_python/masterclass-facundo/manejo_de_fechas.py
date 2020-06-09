import datetime

my_day = datetime.date.today()
print(my_day)

my_day1 = datetime.datetime.now()
print(my_day1)

my_day2 = datetime.date(1999, 12, 23) #crear objetos tipo fecha personalisados
print(my_day2)

my_timestamp = datetime.date.fromtimest(13124214)) 
print(my_timestamp)

my_day3 = datetime.date.today()
print(f'Year: {my_day3.year}')
print(f'Month: {my_day3.month}')
print(f'Day: {my_day3.day}')


my_time = datetime.time.today()
print(f'Houers: {my_day3.year}')
print(f'Minutes: {my_day3.month}')
print(f'Seconds: {my_day3.day}')


