from random import randint

N = int(input('Enter the number '))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
    
print(numbers)
print(numbers[1] * numbers[3])

