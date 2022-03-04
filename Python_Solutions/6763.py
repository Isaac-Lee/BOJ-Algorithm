limit = int(input())
speed = int(input())
if speed <= limit:
    print("Congratulations, you are within the speed limit!")
else:
    over = speed - limit
    fine = 0
    if over < 21:
        fine = 100
    elif over < 31:
        fine = 270
    else:
        fine = 500
    print(f'You are speeding and your fine is ${fine}.')