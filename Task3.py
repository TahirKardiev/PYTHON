def inputCoor(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
                number = float(input(f"Enter {i+1} coordinate: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("It's not")
    return a


def Coordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"The Coordinate is in {text} quarter of the plane")


koordinate = inputCoor(2)
Coordinates(koordinate)