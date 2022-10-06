from tokenize import Double


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
            number = int(input(f"{inputText}"))
            is_OK = True
    return number

def checkNumber(num):
    if 6 <= num <= 7:
        print("Yes")

    elif 0 < num < 6:
        print("No")
    else:
        print("It's not a day of the week")


num = InputNumbers("Enter a days of the week number: ")
checkNumber(num)