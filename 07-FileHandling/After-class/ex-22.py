f = open('txt-ex22.txt', 'a')
import random

counter=1
while counter in range(1,51):
    x=random.randint(100,999)
    f.write(f'{counter}. {x}'+'\n')
    counter+=1