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
        ms=Matches()
        temparr=[]
        for i in value:
            temparr.append(ms.matches.inverse[i])
        i=len(temparr)-1
        while i!=0:
            if temparr[i]>temparr[i-1]:
                temparr[i-1]=-temparr[i-1]
            i=i-1
        return int(sum(temparr))
    

class RomanNum:
    def __init__(self,romanvalue):
        self.romanvalue=romanvalue
    def __str__(self):
        return self.romanvalue
print(Conventer.from_rome_to_arab('XCIX'))
