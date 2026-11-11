import sys

#contains iterable of all lines
inputs = iter(sys.stdin.readlines())


while(True):

    current_line = list(map(int, next(inputs).split()))

    if (len(current_line) == 1 and current_line[0] == 0):
        break

    num_houses = current_line[0]
    midpoint = list(map(int, next(inputs).split()))

    for _ in range(num_houses):
        house = list(map(int, next(inputs).split()))

        if house[0] == midpoint[0] or house[1] == midpoint[1]:
            print("divisa")
        elif house[0] > midpoint[0] and house[1] > midpoint[1]:
            print("NE")
        elif house[0] > midpoint[0] and house[1] < midpoint[1]:
            print("SE")
        elif house[0] < midpoint[0] and house[1] > midpoint[1]:
            print("NO")
        elif house[0] < midpoint[0] and house[1] < midpoint[1]:
            print("SO")

        
                







