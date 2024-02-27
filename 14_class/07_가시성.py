# 가시성 : 정보은닉
# 비공개 필드, 비공개 메서드
# 비공개 필드는 직접 접근가능한 메서드를 구현하여 사용하거나
# 데코레이터(@property) 를 이용하여 직접 사용

class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []

    def addNewItem(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            print('error')
    def showinvent(self):
        print(self.__items)
    def getNumberOfItems(self):
        return len(self.__items)

    # 데코레이터 (@property)를 사용하여 비공개필드를 직접 접근
    @property
    def items(self):
        return self.__items

myinvent = Inventory()
myinvent.addNewItem(Product())
myinvent.addNewItem(Product())
myinvent.addNewItem(Product())

myinvent.showinvent()
# print(myinvent.__items)
print(myinvent.items)

    
