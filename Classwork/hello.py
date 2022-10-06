""" value = None
print(type(value))

a = 123
b = 1.23
print(type(a))
print(type(b))
value=12334
print(type(value))
s = 'hw'

print(s) # input string
print(a, b, s)
print(f'{a} - {b} - {s}')

f = True
print(f)
list = [1, 2 , 3]
print(list) """

""" print('Enter a');
a = float (input()) #int for natural 
print('Enter b');
b = float (input())
print(a+b)
print('{} {}'.format(a ,b))
print(f'{a} {b}') """

""" print('Enter a');
a = int (input())
print('Enter b');
b = int (input())
if a > b:
    print(a)
else:
    print(b) """

""" original = 23
inverted = 0
while original != 0: # ne ravno nulyu
    inverted = inverted * 10 + (original % 10)
    original //=10 # celochislennoe delenie
print(inverted)    
 """

for i in range (1, 10, 2):
    print(i)

def f(x):
    if x ==1:
        return 'Celoe'
    else:
        return

arg = 5
print(f(arg))
print(type(f(arg)))