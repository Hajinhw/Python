# 객체의 필요성

class AddCal:

    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


myadder = AddCal()
myadder.adder(10)
myadder.adder(20)
myadder.adder(30)
print(myadder.result)

youradd = AddCal()
print(youradd.result)
youradd.adder(100)
print(youradd.result)

print(type(myadder))