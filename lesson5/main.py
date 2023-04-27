def restore(arr):
  s=len(arr)-1
  num=0
  i=0
  while s!=-1:
      num+=arr[i]*10**s
      s-=1
      i+=1
  return num
def find_max(*args):
    if args:
      arr=[]
      for i in args:
          k=i
          litle_arr=[]
          while k!=0:
            j=k%10
            k=k//10
            litle_arr.insert(0,j)
          arr.append(litle_arr)
      arr= sorted(arr,reverse=True)
      newarr=[]
      for i in range(len(arr)):
         for j in range(len(arr[i])):
            newarr.append(arr[i][j])
      num=restore(newarr)
      return num
    else:
       print('no data')
# список списков
print(find_max(12,34,567))



         