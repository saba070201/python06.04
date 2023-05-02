class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def __str__(self) -> str:
        return str(f"{self.x},{self.y}")
    def __add__(self,other):
        return Line(self,other)


class Line:
    def __init__(self,p1:Point,p2:Point) -> None:
        self.p1=p1
        self.p2=p2
    def __str__(self) -> str:
        return self.p1.__str__() +','+ self.p2.__str__()
    

p1=Point(1,2)
p2=Point(2,3)
l=Line(p1,p2)
print(l)
p3=p1+p2
print(p3)