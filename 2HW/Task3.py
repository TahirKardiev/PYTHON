s = ""
n = int(input("Enter the number:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)