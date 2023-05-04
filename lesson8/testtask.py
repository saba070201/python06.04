from bidict import bidict


class Matches:
    matches=bidict({1:'I',5:'V',10:'X',50:'L',100:'C'})

class RomanValueError(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message
    
class Conventer:
    @staticmethod
    def from_arab_to_rome(value):
        return RomanNum(value)
    @staticmethod
    def from_rome_to_arab(value):
        
        return int(value)
    

class RomanNum:
    def __init__(self,romanvalue):
        self.choises=['I','V','X','L','C','M']
        self.romanvalue=romanvalue
        
m=Matches()
print(m.matches[5])