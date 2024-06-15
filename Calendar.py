import calendar
for i in range(1970,2025):
    c=calendar.TextCalendar(calendar.MONDAY)
    wx=c.pryear(i)
    print(wx)
    for j in range(50):
        print()
#Calendar



