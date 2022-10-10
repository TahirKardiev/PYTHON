num = int(input("Enter the number: "))
i = 2
lst = []
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Prime factors of a number {num} in list: {lst}")