float_num = input('Enter the number: ')
sum = 0
for i in float_num:
    if i != ',':
        sum += int(i)
print(sum)