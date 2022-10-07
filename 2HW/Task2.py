from multiprocessing.resource_sharer import stop
from platform import java_ver
from random import randint

s = randint(3, 10)

def random_range_of_numbers (numbers, s):  
    for i in range(s):
        numbers.append(randint(1, 10))
    print (numbers)


def multiplication_of_pairs (numbers, s):          
    for i in range(len(numbers)):
        while i < len(numbers)/2 and s > len(numbers)/2:
            s = s - 1
            a = numbers[i] * numbers[s]
            print(a)
            i += 1
           
numbers = []

random_range_of_numbers (numbers, s)
multiplication_of_pairs (numbers, s)