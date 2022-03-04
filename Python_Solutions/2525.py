from datetime import datetime, timedelta
now = datetime.strptime(input(), "%H %M")
after = now + timedelta(minutes=int(input()))
print(after.strftime("%-H %-M"))
