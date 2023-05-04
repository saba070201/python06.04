# try:
#     a=int(input('введите число'))
# except:
#     print('возникла ошибка')
#     a=1
# else:
#     print('ошибки нет')
# finally:
#     print('программа закончила свою работу')
# B=''
# try:
#   assert isinstance(B,int)
# except:
#     B=int(1)
# raise ValueError
class MyEx(Exception):
    def __init__(self,message):
        super().__init__()
        self.message=message
    def __str__(self) :
        return self.message
print(1/0)