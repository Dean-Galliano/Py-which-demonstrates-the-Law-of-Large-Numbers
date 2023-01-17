import random

num=int(input("type the number"))
zero=0
one=0
rate_zero=0
rate_one=0

for i in range(num):
    result=random.randint(0,1)
    if result==0:
        zero+=1
    elif result==1:
        one+=1
    rate_zero=(zero/num)*100
    rate_one=(one/num)*100
        
        
print(f"Done, zero: {zero},one: {one}")
print(f"Rates are zero:{rate_zero}% and one: {rate_one}%")
