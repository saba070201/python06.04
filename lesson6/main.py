import numpy as np
import random
PATH_100='lesson6/arrays/100.txt'
PATH_1000='lesson6/arrays/1000.txt'
PATH_10000='lesson6/arrays/10000.txt'
PATH_100000='lesson6/arrays/100000.txt'
PATH_1000000='lesson6/arrays/1000000.txt'
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

