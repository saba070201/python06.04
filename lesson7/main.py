# class Person:
#     name=''
#     age=0
#     def go(self):
#       print('go')
# p1=Person()
# p1.name='Misha'
# p1.age=22
# p2=Person()
# p2.name='Daniil'
# p2.age=24
# print(p1.name,p1.age)
# print(p2.name,p2.age)
# p1.go()
# p2.go()
class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def __str__(self) -> str:
        return str(f'{self.x=},{self.y=}')


class Line:
    def __init__(self,p1:Point,p2:Point) -> None:
        self.p1=p1
        self.p2=p2
    def __str__(self) -> str:
        return self.p1.__str__() + self.p2.__str__()
    

p1=Point(1,2)
p2=Point(2,3)
l=Line(p1,p2)
print(l)
