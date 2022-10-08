import calendar
yy = int(input())
mm = int(input())
if mm <= 12:
    print(calendar.month(yy, mm))
else:
    print("There're 12 months in the year only!")