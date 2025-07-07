import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

today = datetime.date.today()
print("Today's date:", today)

current_time = datetime.datetime.now().time()
print("Current time:", current_time)

d = datetime.date(2023, 7, 7)
print("Specific date:", d)

dt = datetime.datetime(2023, 7, 7, 12, 30, 45)
print("Specific date and time:", dt)


formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted)

#Parse...

date_string = "2025-07-07 14:32:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date and time:", parsed_date)