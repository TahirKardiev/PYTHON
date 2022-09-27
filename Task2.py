def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Enter value {xyz[i]}: "))
    return a


def Predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


countvalues = inputNumbers(3)

if Predicate(countvalues) == True:
    print(f"True")
else:
    print(f"False")