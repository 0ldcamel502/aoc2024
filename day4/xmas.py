def get_data(file_name: str):
    with open(file_name) as file:
        data = []
        for line in file:
            data.append([line.strip()[i] for i in range(len(line.strip()))] + ["*"])
        data.append(["*" for i in range(len(data[0]))])
    return data

def check_xmas(i, j, data):
    try: 
        if data[i][j] == "M" and data[i][j + 2] == "M" and data[i + 1][j + 1] == "A" \
            and data[i + 2][j] == "S" and data[i + 2][j + 2] == "S":
            return True
    except IndexError:
        return False

def rotate_data(data):
    transposed = list(zip(*data))
    rotated = [list(row)[::-1] for row in transposed]
    return rotated

def get_count(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if check_xmas(i, j, data):
                count += 1
    return count

def main(file_name):
    data = get_data(file_name)
    count = 0
    for i in range(4):
        count += get_count(data)
        data = rotate_data(data)

    print(count)

if __name__ == "__main__":
    main("data.txt")