lst = list(map(int, input("Enter the numbers through gap:\n").split()))
print(f"Numbers: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"List of none-repeat numbers: {new_lst}")