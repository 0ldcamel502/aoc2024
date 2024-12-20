import time
class Karel:
    def __init__(self, row: int, col: int, symbol: str, map_grid: list):
        self.row = row
        self.col = col
        self.symbol = symbol
        self.map_grid = map_grid
        # self.loop = {">": 0, "<": 0, "^": 0, "v": 0}

    def get_direction(self):
        directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
        return directions[self.symbol]

    def get_position(self):
        return self.row, self.col

    def if_front_is_clear(self):
        dlt_row, dlt_col = self.get_direction()
        if self.map_grid[self.row + dlt_row][self.col + dlt_col] in [".", "X", "|", "-", "+"]:
            return "go"
        elif self.map_grid[self.row + dlt_row][self.col + dlt_col] == "#":
            return "turn"
        elif self.map_grid[self.row + dlt_row][self.col + dlt_col] == "O":
            return "O"    
        else:
            return "over"
        
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
        i_e = min(i_s + 20, 130)

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
        return f'{self.row}, {self.col}, {self.symbol}'
    
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
        try:
            if karel.if_front_is_clear() == "go":
                karel.put_beeper()
            elif karel.if_front_is_clear() == "turn":
                karel.turn_right()
                karel.put_beeper_corner()
            elif karel.if_front_is_clear() == "O":
                karel.turn_right()
                karel.put_beeper_corner()
            elif karel.if_front_is_clear() == "over":
                raise IndexError
            karel.move()
            x, y = karel.get_position()
            symbol = karel.get_direction()
            if (x, y, symbol) in breadcrumbs:
                return True
            else:
                breadcrumbs[(x, y, symbol)] = 1

            if x < 0 or x > m or y < 0 or y > n:
                raise IndexError
            
        except IndexError:
            karel.put_beeper()
            break

def get_map():
    map_grid = []
    with open("p1sdata.txt") as file:
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
    start_time = time.time()
    count = 0
    map_grid = get_map()
    m, n = len(map_grid), len(map_grid[0])
    for i in range(m):
        for j in range(n):
            if is_loop(i, j):
                count += 1
    print("total position count:", count)
