# from colorama import Fore
# print(Fore.RED)
# # # # PASSWORD='password'
# # # # check=False
# # # # count_of_input=0
# # # # while True:
# # # #     prepassword=input('Введите пароль:')
# # # #     if prepassword==PASSWORD:
# # # #       check=True
# # # #       print(check)
# # # #       print('пароль верный')
# # # #       break
# # # #     else:
# # # #       print('пароль не верный')
# # # #       count_of_input+=1 # эквивалентно count_of_input=count_of_input+1
# # # #       if count_of_input>=2:
# # # #          print('превышено количество попыток')
# # # #          break
# # # # a=0
# # # # while a<10:
# # # #     print(a)
# # # #     a+=1
# # # #Вывести числа от k до n не включительно  c помощью цикла while 
# # # k=int(input())
# # # n=int(input())
# # # while k<n:
# # #     print(k)
# # #     k=k+1
# # #     # k=k-1
# # #     # k-=1
# # # word='simpleword'

# # for i in 'word','hello','baza':
# #     for j in i:
# #         print(j)
# # # print(word[0],word[1],word[2],word[3])
# # посчитать сумму чисел от n до k
# # n=int(input())
# # k=int(input())
# # sum=1
# # while n<=k:
# #     sum*=n
# #     n+=1
    
# # print(sum)
# # l=[1,4,'hello',[6,7,11],[326,[1,2,[7,'baza']]]]
# # print(l[4][1][2][1]) # out:baza
# l=[1,2,3]
# l1=[1,2,3]
# # l.append(1) # добавление нового элемента в массив 
# # l.append(2)
# # l.append(3)
# # print(l[0])
# index=0
# for i in l:
#     l[index]=i**2
#     index+=1
# print(l,'by bad practice')
# for i in range(len(l)):
#     l1[i]=l1[i]**2
# print(l1,'by range')
# l2=[1,2,3]
# l3=l2.copy()
# l3[1]=10
# print(id(l1),id(l2))
# задача на поиск максимума 


# max_elem=l[0]
# for i in range(len(l)):
#     if l[i]>max_elem:
#         max_elem=l[i]
# print(max_elem)

# print(l[1:4:])
# Есть массив элементов. Раскидать элементы меншьие и большие опорного по разным массивам. Сделать опорным элементом значение из серединного индека (тут поможет деление нацело (//))
# l_start=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
# k=l_start[len(l_start)//2]
# l_less=[]
# l_more=[]
# for i in range(len(l_start)):
#     if l_start[i]>=k:
#         l_more.append(l_start[i])
#     else:
#         l_less.append(l_start[i])
# print(k,l_less,l_more)
# задача : Создать новый массив из элементов под четным индексом.