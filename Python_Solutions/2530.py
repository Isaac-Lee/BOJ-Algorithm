from datetime import datetime, timedelta
now = datetime.strptime(input(), "%H %M %S")
after = now + timedelta(seconds=int(input()))
print(after.strftime("%-H %-M %-S"))
