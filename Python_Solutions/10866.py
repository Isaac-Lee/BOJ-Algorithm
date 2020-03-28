import collections


class water:
    def __init__(self):
        self.deque = collections.deque()

    def push_back(self, num):
        self.deque.append(num)

    def push_front(self, num):
        self.deque.appendleft(num)

    def pop_front(self):
        if self.deque:
            return self.deque.popleft()
        else:
            return -1

    def pop_back(self):
        if self.deque:
            return self.deque.pop()
        else:
            return -1

    def size(self):
        return len(self.deque)

    def empty(self):
        if self.deque:
            return 0
        else:
            return 1

    def front(self):
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def back(self):
        if self.deque:
            return self.deque[-1]
        else:
            return -1


test = int(input())
case = water()
result = []
for i in range(test):
    a = input()
    if " " in a:
        a, b = a.split()

    if a == "push_back":
        case.push_back(b)
    elif a == "push_front":
        case.push_front(b)
    elif a == "pop_front":
        result.append(case.pop_front())
    elif a == "pop_back":
        result.append(case.pop_back())
    elif a == "size":
        result.append(case.size())
    elif a == "empty":
        result.append(case.empty())
    elif a == "front":
        result.append(case.front())
    elif a == "back":
        result.append(case.back())

for i in result:
    print(i)