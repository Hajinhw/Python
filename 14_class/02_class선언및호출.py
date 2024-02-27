# 클래스 선언
# class 클래스명(상속클래스):
#     클래스 변수(필드) 선언
#     메서드 정의
#     def 메서드 이름(self, 매개변수들):
#         문장들

# 객체(인스턴스) 생성
# 이름 = 클래스명() : 생성자

# 객체 : 단독으로 객체만 지칭
# 인스턴스 : 클래스와 연관지어서 부를 때

# 예. 자동차 클래스 선언

class Car:
    color = ''
    speed = 0
    def drive(self):
        self.speed = 10

# 필드(변수)
# 메서드 정의
# self : 기존의 함수와 구분, 자신의 객체(인스턴스)임을 의미

car1 = Car()        # Car() : 인스턴스 생성하는 생성자 함수
car2 = Car()
car3 = Car()

print(type(car1), id(car1))
print(type(car2), id(car2))
print(type(car3), id(car3))

# isinstance(인스턴스명, 클래스명) : 특정 클래스의 인스턴스인지 확인
print(isinstance(car1, Car))

# car1.drive()
print(car1.speed)
print(car2.speed)
print(car3.speed)

# 인스턴스 생성 후 필드 추가하고 값을 대입할 수 있음
# car1.color = 'red'
# car2.color = 'blue'
# car3.color = 'yellow'
# car1.speed = 0
# car2.speed = 0
# car3.speed = 0
# print(car1.color)

# 파이썬의 클래스들 : int, float, str, set, dict, list, ...

