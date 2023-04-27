a=10# целое число int
b=10.12515 # вещественное число float 
name='Misha' # строка str
coonect=True # булево значение 
print(a,b,name,coonect)
a=15
b=20
c=a-b
# print(c)
a=int(input('Введите переменную "a":'))
b=a-10
print(b)
a=12
b=11
if a<b:
  print('ok')
print(a<b)
a=-10
b=-1
result=(a<b)*a+(b<a)*b
print(result)
Условие задачи: допустим, у нас есть оптика. Мы прорабатываем систему лояльности по следующим критериям: пенсионерам женщинам - скидка 25%, пенсионерам мужинам -10%. Детям мальчикам - 30 % , детям девочкам - 5%. Совершеннолетнему - 15%. Допустим в магазине есть лишь один товар, у него есть цена. Найти цену после применения скидки. 
name=str(input('name:'))
age=int(input('age:'))
male_or_female=str(input('male/female:'))
discount=0
if male_or_female=='male':
    if age >= 65:
        discount=10
    elif 18<=age<65:
        discount=15
    else:
        discount=30
elif male_or_female=='female':
    if age >= 60:
        discount=25
    elif 18<=age<60:
        discount=15
    else:
        discount=5
else:
    print('error!!!')
print('Привет',name,'твоя скидка',discount,'%')
print(f'Привет {name} твоя скидка {discount}%')
есть стороны a,b,c . Узнать: можно ли построить из этих сторон треугольник ? 
a=int(input())
b=int(input())
c=int(input())
triangle_or_not=False
if a+b>c and c+a>b and b+c>a:
    triangle_or_not=True
    print('треугольник существует')
    if a==b==c:
        print('треугольник равносторонний')
    elif a==b or b==c or a==c:
        print('треугольник равнобедренный')
    else: 
        print('треугольник разносторонний')
    if a**2+b**2==round(c**2):
        print('треугольник прямоугольный')
    else:
        print('треугольник не прямоугольный')
else: 
    print('треугольника не существует')
a=0
check=True
while check:
    print('ok')
    a=a+1
    if a>20:
        check=False
   
   
