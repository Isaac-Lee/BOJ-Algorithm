for i in range(3):
    order = list(map(int, input().split()))
    if order.count(0) == 1:
        print("A")
    elif order.count(0) == 2:
        print("B")
    elif order.count(0) == 3:
        print("C")
    elif order.count(0) == 4:
        print("D")
    else:
        print("E")