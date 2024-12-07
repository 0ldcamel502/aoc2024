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
        if self.map_grid[self.row + dlt_row][self.col + dlt_col] in [".", "X"]:
            return True
        elif self.map_grid[self.row + dlt_row][self.col + dlt_col] == "#":
            return False
        else:
            return "over"
        
    def move(self):
        dlt_row, dlt_col = self.get_direction()
        if self.if_front_is_clear():
            self.row += dlt_row
            self.col += dlt_col
            self.map_grid[self.row][self.col] = self.symbol

    def put_beeper(self):
        row, col = self.row, self.col
        self.map_grid[row][col] = "X"
    
    def print_map(self):
        for row in self.map_grid:
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

def main():
    map_grid = get_map()
    row, col, symbol = find_karel(map_grid)
    karel = Karel(row, col, symbol, map_grid)

    while True:
        karel.print_map()
        try:
            if karel.if_front_is_clear():
                karel.put_beeper()
                karel.move()
            else:
                karel.turn_right()
                karel.put_beeper()
                karel.move()
        except IndexError:
            karel.put_beeper()
            print("Dear Lord Karel, there are",karel.count_beepers(), "beepers.")
            break
        time.sleep(.2)
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
    main()
