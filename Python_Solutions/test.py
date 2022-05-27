class A:
    def __init__(self, i):
        self.i = i
        pass

    def __gt__(self, other):
        print("A.__gt__() called")
        return self.i > other.i


class B(A):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j

    def __lt__(self, other):
        print("B.__lt__() called")
        return self.j < other.j

a = A(1)
b = B(2, 3)

var = a > b
print(var)
