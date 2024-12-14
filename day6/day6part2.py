import time
class Karel:
    def __init__(self, row: int, col: int, symbol: str, map_grid: list):
        self.row = row
        self.col = col
        self.symbol = symbol
        self.map_grid = map_grid

    def get_direction(self):
        directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
        return directions[self.symbol]

    def get_position(self):
        return self.row, self.col

    def if_front_is_clear(self):
        dlt_row, dlt_col = self.get_direction()
        if self.map_grid[self.row + dlt_row][self.col + dlt_col] in [".", "X", "|", "-", "+"]:
            return True
        elif self.map_grid[self.row + dlt_row][self.col + dlt_col] in ["#", "O"]:
            return False
        
    def move(self):
        dlt_row, dlt_col = self.get_direction()
        self.row += dlt_row
        self.col += dlt_col
        self.map_grid[self.row][self.col] = self.symbol

    def put_beeper(self):
        row, col = self.row, self.col
        symbol = self.symbol
        if symbol in [">", "<"]:
            self.map_grid[row][col] = "-"
        elif symbol in ["^", "v"]:
            self.map_grid[row][col] = "|"
    
    def put_beeper_corner(self):
        row, col = self.row, self.col
        self.map_grid[row][col] = "+" 

    def print_map(self):
        i, j = self.get_position()
        i_s = max(0, i - 10)
        i_e = min(i_s + 20, len(self.map_grid))

        for k in range(i_s, i_e):
            row = self.map_grid[k]
            [print(item, end="") for item in row]
            print()
        print()

    def turn_right(self):
        symbols = [">", "v", "<", "^"]
        index = symbols.index(self.symbol)
        self.symbol = symbols[(index + 1) % 4]

    def __str__(self):
        return f'Karel is at {self.row}, {self.col}, facing {self.symbol}'
    
    def count_beepers(self):
        beepers = 0
        for row in self.map_grid:
            beepers += row.count("X")
        return beepers

    def set_obstruction(self, row, col):
        self.map_grid[row][col] = "O"

def is_loop(i, j):
    map_grid = get_map()
    m, n = len(map_grid), len(map_grid[0])
    row, col, symbol = find_karel(map_grid)
    karel = Karel(row, col, symbol, map_grid)
    karel.set_obstruction(i, j)
    breadcrumbs = {}
    while True:
        # karel.print_map()
        # print(karel, "obstruction placed at:", i, j)
        # time.sleep(0.01)
        try:
            turn = "no"
            rotate_count = 0
            while not karel.if_front_is_clear():
                karel.turn_right()
                rotate_count += 1
                turn = "yes"
            
            if turn == "yes":
                karel.put_beeper_corner()
            else:
                karel.put_beeper()
            karel.move()

            x, y = karel.get_position()
            symbol = karel.symbol
            if (str(x) + str(y) + symbol) in breadcrumbs:
                breadcrumbs[str(x) + str(y) + symbol] += 1
                if breadcrumbs[str(x) + str(y) + symbol] > 2:
                    # print("breadcrumb =", breadcrumbs[str(x) + str(y) + symbol])
                    return True
            else:
                breadcrumbs[str(x) + str(y) + symbol] = 1
                # with open("bread.txt", "a") as bread:
                #     bread.write(f"{x}, {y}, {symbol}\n")

            if x < 0 or x > m or y < 0 or y > n:
                raise IndexError
            
        except IndexError:
            break
        

def get_map():
    map_grid = []
    with open("data.txt") as file:
        for line in file:
            row = [c for c in line.strip()]
            map_grid.append(row)
        return map_grid

def find_karel(map_grid):
    symbols = [">", "v", "<", "^"]
    for i in range(len(map_grid)):
        for j in range(len(map_grid[0])):
            if map_grid[i][j] in symbols:
                return i, j, map_grid[i][j]

if __name__ == "__main__":
    # start_time = time.time()
    count = 0
    map_grid = get_map()
    m, n = len(map_grid), len(map_grid[0])
    for i in range(m):
        for j in range(n):
            if is_loop(i, j):
                count += 1
                print(count, i, j)
                with open("camel.txt", "a") as output:
                    output.write(f"{count}, {i}, {j}\n")
    print("total position count:", count)
