import random
import math
import time
import json
def game(interval=128,name='undefined'):
    count_of_attempt=math.log(interval,2)-1
    answer_num=random.randint(0,128)
    
    user_count_of_attempt=0
    score=count_of_attempt+1
    start_time=time.time()
    while user_count_of_attempt < count_of_attempt:
        user_num=int(input('введите число'))
        score-=1
        user_count_of_attempt+=1
        if user_num==answer_num:
            print('вы угадали')
            break
        elif user_num > answer_num:
            print('ваше число больше')
        elif user_num < answer_num:
            print('ваше число меньше')
    end_time=time.time()
    final_time=round(end_time-start_time,2)
    return {'user':name,'interval':interval,'attempts':{'total':count_of_attempt,'total_user':user_count_of_attempt},'score':score,'time':final_time}
def make_stat_file(data):
    with open ('lesson4/results/count.json','r') as f:
        count=json.load(f)
        count["count"]+=1
        num=count["count"]
    with open('lesson4/results/count.json','w') as f1:
        json.dump({"count":count["count"]},f1)
    with open(f'lesson4/results/result{num}.json','w') as f:
        json.dump(data,f)
    
data=game()
make_stat_file(data)
        
