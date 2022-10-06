from random import randint

def random_range_of_numbers (numbers):
    for i in range(randint(2, 10)):
        numbers.append(randint(1, 10))
    print (numbers)

def sum_odd_index(numbers):
    si = 0
    for i in range(len(numbers)):
        if i % 2 != 0:
            si += numbers[i]
    print(f"Summ: {si}")

numbers = []
random_range_of_numbers(numbers)
sum_odd_index(numbers)

