from datetime import datetime
while True:
    s = input()
    if s == '0 0 0':
        break
    try:
        datetime.strptime(s, '%d %m %Y')
        print('Valid')
    except:
        print('Invalid')