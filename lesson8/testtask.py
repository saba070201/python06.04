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
        value=str(value)
        value=[i for i in value]
        ms=Matches()
        romans = list([ i for i in ms.matches.inverse])
     
        str_arabic = value[::-1]
        str_arabic_len = len(str_arabic)
        result = str()
        romans_pointer = 0
        for i in range(str_arabic_len):
            if str_arabic[i] in ['0', '1', '2', '3']:
                result = romans[romans_pointer] * int(str_arabic[i]) + result
            elif str_arabic[i] in ['4']:
                result = romans[romans_pointer] + romans[romans_pointer + 1] + result
            elif str_arabic[i] in ['5', '6', '7', '8']:
                result = romans[romans_pointer + 1] + romans[romans_pointer] * (int(str_arabic[i]) - 5) + result
            elif str_arabic[i] in ['9']:
                result = romans[romans_pointer] + romans[romans_pointer + 2] + result
            romans_pointer += 2
        return result
    

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
    def check(self,checkvalue):
        m=Matches()
        matches=[i for i in m.matches.inverse ]
        for i in checkvalue:
            if i not in matches:
                return False
        return True
    def __init__(self,value):
        if isinstance(value,int):
            self.arabicvalue=value
            self.romanvalue=Conventer.from_arab_to_rome(value)
        elif isinstance(value,str):
            try:
              assert self.check(value)
            except RomanValueError('такого числа не существует') as e:
              print(e)
            else:
              self.arabicvalue=Conventer.from_rome_to_arab(value)
              self.romanvalue=value
    def __str__(self):
        return str(self.romanvalue)+'!'+str(self.arabicvalue)
    def __add__(self,other):
        if isinstance(other,RomanNum):
            return RomanNum(self.arabicvalue+other.arabicvalue)
        elif isinstance(other,int):
            return self.arabicvalue+other
    
r=RomanNum('X')+10
r=RomanNum(r)
print(r)