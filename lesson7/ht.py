import random
from abc import ABC,abstractmethod
import math

class Hero(ABC):
    @abstractmethod
    def beat(self):
        pass
    

class Sword:
    def __init__(self,name,attack):
        self.name=name
        self.attack=attack


class Warior(Hero):
    def __init__(self,name,hp,attack,sword):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.sword=sword
    def beat(self,other:'Warior'):
        other.hp-=(self.attack+self.sword.attack)

class Archer(Hero):
    def __init__(self,name,hp,attack,chance):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.chance=chance
    def beat(self,other):
        check=random.randint(1,100)
        attack=self.attack
        if check <=self.chance:
            attack=self.attack*2
            print('критическая атака')
        other.hp-=attack
        
        
        

class Batle:
    @staticmethod
    def batle(p1,p2):
      while True:
          if p1.hp <=0:
              print(f'{p2.name} победил')
              break
          if p2.hp <=0:
              print(f'{p1.name} победил')
              break
          who=random.randint(0,1)
          if who == 0:
              p1.beat(p2)
              print(f'{p1.name} бьет {p1.attack} {p2.hp}')
          elif  who ==1:
              p2.beat(p1)
              print(f'{p2.name} бьет {p2.attack} {p1.hp}')


w1=Warior('Artes',1000,10,Sword('frostmorn',10))
w2=Warior('Silvana',500,20,Sword('?',20))
Batle.batle(w1,w2)
