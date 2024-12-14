from itertools import product
import time
data_file = "day7data.txt"

start = time.time()
def get_data(data_file):
    data = {}
    with open(data_file) as file:
        for line in file:
            left, right = line.strip().split(":")
            parts = right.strip().split(" ")
            parts = [int(item) for item in parts]
            data[int(left)] = parts
    return data

def get_sum(a, b):
    return a + b

def get_mul(a, b):
    return a * b

def get_con(a, b):
    return int(str(a) + str(b))

def get_permutations_of_operators(a_list):
    n = len(a_list)
    return list(product(["+", "x", "|"], repeat=n-1))

def make_calculations(i, a_list):
    operators = get_permutations_of_operators(a_list)[i]
    ope_dict = {"+": get_sum, "x": get_mul, "|": get_con}
    result = a_list[0]
    # output = f'{a_list[0]} '
    for i in range(len(operators)):
        result = ope_dict[operators[i]](result, a_list[i + 1])
        # output += f'{operators[i]} {a_list[i + 1]} '
    # print(output, "=", result)
    return result


def is_solvable(a_line):
    left, right = a_line
    n = len(get_permutations_of_operators(right))
    for i in range(n):    
        if left == make_calculations(i, right):
            # print(left)
            return left
        

def total_result():
    data = get_data(data_file)
    lines = [key for key in data.items()]
    total = 0
    n = len(lines)
    for i in range(n):
        m = is_solvable(lines[i])
        if m:
        # if is_solvable(lines[i]):
            # total += is_solvable(lines[i])
            total += m

    print("total result is:", total)

total_result()
end = time.time()
print(end - start)