def get_data(file_name: str):
    data = []
    with open(file_name) as file:
        for row in file:
            data.append("*" + row.strip() + "*")
        data.append("*" * len(data[0]))
    return data

def direction(index_x: int, index_y: int, data: list, direction: tuple):
    try:
        output = ""
        for i in range(len("XMAS")):
            output += data[index_x + i * direction[0]][index_y + i * direction[1]]
        if output == 'XMAS':
            return True
    except IndexError:
        return False




directions = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]

output = []

def main(file_name):
    data = get_data(file_name)
    count = 0
    for dir in directions:
        for i in range(len(data)):
            for j in range(len(data[i])):
                if direction(i, j, data, dir):
                    count += 1
                    # file.write(f'{i}, {j}, {(dir)}, "count = ", {count}\n')
                    # output.append([i, j, dir])

    print("count:",count)        

# for i in range(2000,2100):
#     print(output[i], i)
#     print_output(output[i], data)    
# with open("output.csv", "w") as file:
main("data.txt")