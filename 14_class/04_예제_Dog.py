# 예제. Dog 클래스

class Dog:
    dog_id = 0      # 클래스 변수
    def __init__(self, name, breed, size, age, color):
        self.name = name
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
        self.dog_id = self.dog_id + 1

    def eat(self, food):
        print(f'{self.name}이(가) {food}를 먹는다')

    def sleep(self):
        print(f'{self.name}이(가) 잠잔다')

    def sit(self):
        print(f'{self.name}이(가) 앉아있다')

    def run(self):
        print(f'{self.name}이(가) 뛴다')

    def __repr__(self):
        return f'{self.name}의 품종은 {self.breed}이다.'

dog1 = Dog('삐삐', 'Maltese', 'small', 2, 'white')
dog2 = Dog('벤', '추추', 'medium', 3, 'brown')
dog3 = Dog('뭉치', '진돗개', 'medium', 1, 'white')

dog1.eat('개껌')
dog2.sit()

print(dog1.name)
print(dog1)

print(dog1.dog_id)
print(dog2.dog_id)

# 인스턴스 변수 : 인스턴스가 소유하고 있는 변수
# 클래스 변수 : 전역변수와 같이 클래스의 모든 인스턴스들이 공유하는 변수
#   클래스이름.클래스변수명 으로 메서드 내부에서 사용하고
#   인스턴스이름.클래스변수명으로 사용