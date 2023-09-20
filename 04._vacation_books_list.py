pages = int(input())
pages_hour = int(input())
days = int(input())

total_hours = pages / pages_hour
day_Hours = total_hours // days

print(day_Hours)