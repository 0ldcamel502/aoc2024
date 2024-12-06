def print_output(an_output, data):
    index_x, index_y , dir = an_output[0], an_output[1], an_output[2]
    if dir[0] == 0:
        if dir[1] == 1:
            print(data[index_x][index_y: index_y + 4])
        elif dir[1] == -1:
            print(data[index_x][index_y - 3: index_y + 1])
    elif dir[0] == 1:
        if dir[1] == 0:
            for i in range(4):
                print(data[index_x + i][index_y])
        elif dir[1] == 1:
            for i in range(4):
                print(data[index_x + i][index_y: index_y + 4])
        elif dir[1] == -1:
            for i in range(4):
                print(data[index_x + i][index_y - 3: index_y + 1])
    elif dir[0] == -1:
        if dir[1] == 0:
            for i in range(4):
                print(data[index_x + i - 3][index_y])
        elif dir[1] == 1:
            for i in range(4):
                print(data[index_x + i - 3][index_y: index_y + 4])
        elif dir[1] == -1:
            for i in range(4):
                print(data[index_x + i - 3][index_y - 3: index_y + 1])