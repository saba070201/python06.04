from abc import ABC,abstractclassmethod
class Transport(ABC):
    @abstractclassmethod
    def move(self):
        pass


class Сart(Transport):

    def __init__(self,wheels,body,price):
        self.price=price
        self.wheels=wheels
        self.body=body
    def move(self):
        print('move')


class Car(Сart):
    def __init__(self, wheels, body, price,engine):
        super().__init__(wheels, body, price)
        self.engine=engine
    def move(self):
        print('move')

class Wheel:
    def __init__(self,d,disk,tire):
        self.d=d
        self.disk=disk
        self.tire=tire


class Engine:
    def __init__(self,power) :
        self.power=power


class Disk:
    def __init__(self,title) :
        self.title=title


class Tire:
    def __init__(self,title):
        self.title=title

wheel=Wheel(15,Disk('d1'),Tire('summer'))
engine=Engine(300)
car=Car([wheel,wheel,wheel,wheel],10000,engine,'body')
print(car.wheels[0].tire.title)


