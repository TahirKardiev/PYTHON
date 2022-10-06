colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') #a=add, r=read, w=write(rewrite)
data.writelines(colors)
data.close()


path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

import HelloPython.Task1 as T1

print(T1.f(1))