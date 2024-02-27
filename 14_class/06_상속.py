# 상속 : 부모 클래스로부터 상속받은 필드와 메소드를 이용하거나 추가 변경하여 활용(재사용)
# 메서드 재정의(overriding) : 상속받은 메서드를 다시 정의
'''
class Car(object):
    def __init__(self, speed=0, color=''):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}로 주행한다')


class Truck(Car):
    def __init__(self, speed, color, load):
        super().__init__(speed, color)
        self.load = load


    # 메서드 재정의 (overridinig)
    def drive(self):
        print(f'{self.speed}로 {self.load}양의 짐을 싣고 주행한다')

    def loading(self):
        print(f'최대 {self.load}양의 짐을 운반할 수 있는 트럭')


car1 = Car()
truck1 = Truck(0, 'blue', 5)
truck2 = Truck(0, 'white', 10)
truck3 = Truck(0, 'blue', 5)
for car in [car1, truck1, truck2, truck3]:
    car.drive()
'''
# ---------------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('Subclass muust implement abstract method')

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof Woof!'

animals = [Cat('missy'), Cat('Mr.Mistoffelees'), Dog('zion')]

for animal in animals:
    print(animal.name + ':' + animal.talk())