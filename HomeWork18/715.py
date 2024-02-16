import calendar

year = int(input())
month = int(input())

cal = calendar.monthcalendar(year, month)
month_name = calendar.month_name[month]
print(f"     {month_name} {year}")
print("Mo Tu We Th Fr Sa Su")
for week in cal:
    for day in week:
        if day == 0:
            print("   ", end="")
        else:
            print(f"{day:2} ", end="")
    print()
