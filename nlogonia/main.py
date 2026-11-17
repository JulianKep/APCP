while(True):
    line = list(map(int, input().split()))

    if(line[0]== 0 and len(line) == 1):
        break

    num_examples = line[0]
    coords_center = list(map(int, input().split()))

    for _ in range(num_examples):
        house_coords = list(map(int, input().split()))

        if(house_coords[0] > coords_center[0] and house_coords[1] > coords_center[1]):
            print("NE")
        elif(house_coords[0] > coords_center[0] and house_coords[1] < coords_center[1]):
            print("SE")
        elif(house_coords[0] < coords_center[0] and house_coords[1] > coords_center[1]):
            print("NO")
        elif(house_coords[0] < coords_center[0] and house_coords[1] < coords_center[1]):
            print("SO")
        else:
            print("divisa")
