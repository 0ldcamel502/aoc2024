
def get_map():
    map = []
    with open("p1sdata.txt") as file:
        for line in file:
            row = [c for c in line.strip()]
            map.append(row)
        return map

class Karen:
    map = get_map()

    def __init__(self, row: int, col: int, symbol: str):
        self.row = row
        self.col = col
        self.symbol = symbol

    def get_direction(self):
        directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
        return directions[self.symbol]

    def get_position(self):
        return self.row, self.col

    def if_front_is_clear(self):
        dlt_row, dlt_col = self.get_direction()
        if Karen.map[self.row + dlt_row][self.col + dlt_col] in [".", "X"]:
            return True
        elif Karen.map[self.row + dlt_row][self.col + dlt_col] == "#":
            return False
        else:
            return "over"
        
    def move(self):
        dlt_row, dlt_col = self.get_direction()
        if self.if_front_is_clear():
            self.row += dlt_row
            self.col += dlt_col
            Karen.map[self.row][self.col] = self.symbol

    def put_beeper(self):
        row, col = self.row, self.col
        Karen.map[row][col] = "X"
    
    def print_map(self):
        for row in Karen.map:
            print(row)
        print()

    def turn_right(self):
        symbols = [">", "v", "<", "^"]
        index = symbols.index(self.symbol)
        self.symbol = symbols[(index + 1) % 4]

    def __str__(self):
        return f'{self.row}, {self.col}, {self.symbol}'
    
    def count_beepers(self):
        beepers = 0
        for row in Karen.map:
            beepers += row.count("X")
        return beepers

def find_karen():
    map = get_map()
    symbols = [">", "v", "<", "^"]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in symbols:
                return i, j, map[i][j]

def main():
    row, col, symbol = find_karen()
    karen = Karen(row, col, symbol)

    while True:
        karen.put_beeper()
        karen.print_map()
        try:
            if karen.if_front_is_clear():
                karen.move()
            else:
                karen.turn_right()
                karen.move()
        except IndexError:
            print(karen.count_beepers())
            break

if __name__ == "__main__":
    main()
