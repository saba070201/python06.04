class Car:
    def __init__(self,wheels,price,engine,body):
       

        self.price=price
        self.wheels=wheels
        self.engine=engine
        self.body=body
    

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

# car=Car([Wheel(15,Disk('d1'),Tire('t1')),Wheel(15,Disk('d1'),Tire('t1')),Wheel(15,Disk('d1'),Tire('t1')),Wheel(15,Disk('d1'),Tire('t1')),],1000,Engine(300))
wheel=Wheel(15,Disk('d1'),Tire('summer'))
engine=Engine(300)
car=Car([wheel,wheel,wheel,wheel],10000,engine,'body')
print(car.wheels[0].tire.title)

