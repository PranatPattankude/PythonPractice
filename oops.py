class dived:
    def div(self):
        res = self.a / self.b
        return res


class mul(dived):

    def mul(self):
        res = self.e * self.f
        return res


class maths(mul):
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def add(self):
        res = self.a + self.b
        return res

    def sub(self):
        res = self.c - self.d
        return res


obj = maths(2, 3, 4, 5, 6, 76)
obj1 = maths(45,56,34,32,24,23)
obj2 = maths(32,435,3,23,34,45)

# res = maths.sub(obj)
# print(res)
# print(maths.mul(obj1))
# print(maths.add(obj2))

# print(maths.div(obj))