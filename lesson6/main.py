import numpy as np
import random
import time
PATH_100='lesson6/arrays/100.txt'
PATH_1000='lesson6/arrays/1000.txt'
PATH_10000='lesson6/arrays/10000.txt'
PATH_100000='lesson6/arrays/100000.txt'
PATH_1000000='lesson6/arrays/1000000.txt'
PATH_RESULT='lesson6/arrays/result.txt'

def write_arr_to_file(path,size):
    a=[random.randint(-1000,1000) for i in range(size)]
    with open(path,'w') as f:
        for i in a:
          f.write(str(i)+'\n')
def read_array_from_file(path):
    arr=[]
    with open(path,'r') as f:
        for i in f:
            arr.append(int(i))
    return arr
def writeresult(path,data):
    with open(path,'a+') as f:
        f.write(str(data)+'\n')
def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

temparr=read_array_from_file(PATH_100000)   
stime=time.time()
bubblesort(temparr)
ftime=time.time()
fftime=ftime-stime
writeresult(PATH_RESULT,f'bubblesort100000 {fftime}')