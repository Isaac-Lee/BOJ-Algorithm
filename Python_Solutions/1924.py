from datetime import date
print(date(2007, *list(map(int, input().split()))).strftime('%A').upper()[:3])