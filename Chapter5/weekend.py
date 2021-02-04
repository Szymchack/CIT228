import datetime
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
now = datetime.date.today()
dayOfWeek=now.weekday()
today=weekDays[dayOfWeek]
daysToWeekend=6-dayOfWeek
print("There are ", daysToWeekend-1, " days until the weekend")
quotePrinted="false"
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == "Sunday" and quotePrinted=="false":
        print(left, " Sunday is the Lords day!")
        quotePrinted="true"
    elif (today=="Monday" or today == "Tuesday" or today =="Wednesday") and quotePrinted=="false":
        print(left, " Here I go again on my own!")
        quotePrinted="true"
    elif today =="Thursday" and quotePrinted=="false":
        print(left, " Rounding third on my way home.")
        quotePrinted="true"
    elif quotePrinted=="false":
        print(left, "My chains are gone, I've been set free!")
        quotePrinted="true"
    else:
        print(left)