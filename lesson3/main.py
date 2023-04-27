# # # def test_foo(argument):
# # #     print(argument,'Forever')

# # # test_foo('Hello world')
# # a=id('sfsa')
# # print(type(a))

# # def custom_sum(a,b):
# #     return a+b
# # def custom_sum_1(a,b):
# #     print(a+b)
# # c=custom_sum(2,3)
# # d=custom_sum_1(2,3)
# # print(c,d)
# def find_maximum(arr):
#     max_elem=arr[0]
#     for i in range(len(arr)):
#         if arr[i]>max_elem:
#             max_elem=arr[i]
#     return max_elem
# # l=[1,23623,-1651,0,15,1,23626,-1515,0,-2,144]
# # l1=[12,23,1651,0,15,1,2662626,-1515,99,-22,6]
# # print(find_maximum(l))
# # print(find_maximum(l1))
# def sum_from_n_to_k(n,k):
#     if n>=k:
#         return -1
#     while n<k:
#         print(n)
#         n+=1
#     print('!!!!!!!!!')   
def reverse_list(l):
   
    last=len(l)-1
    first=0
    i=0
    while first <= last:
        # l[first],l[last]=l[last],l[first]
        value=l[first]
        l[first]=l[last]
        l[last]=value
        first+=1
        last-=1
        i+=1
        print(i)
    print(l)
# Написать функцию, находящую средний элемент массива 
reverse_list([1,2,3,4,5,6,7,8,9,10])

def find_average(l):
    sum=0
    for i in l:
        print(i)
        sum=sum+i
    average=sum/len(l)
    return average
print(find_average([1,2,10,4]))