import copy
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
        self.loop = {">": 0, "<": 0, "^": 0, "v": 0}

    def count_loop(self):
        direction = self.symbol
        self.loop[direction] += 1

    def get_loop_count(self):
        loop = self.loop
        return max(loop.values())

    def get_direction(self):
        directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
        return directions[self.symbol]

    def get_position(self):
        return self.row, self.col

    def if_front_is_clear(self):
        dlt_row, dlt_col = self.get_direction()
        if Karen.map[self.row + dlt_row][self.col + dlt_col] in [".", "X", "|", "-", "+"]:
            return True
        elif Karen.map[self.row + dlt_row][self.col + dlt_col] == "#":
            return "turn"
        elif Karen.map[self.row + dlt_row][self.col + dlt_col] == "8":
            return "8"
        else:
            raise IndexError
        
    def move(self):
        dlt_row, dlt_col = self.get_direction()
        if self.if_front_is_clear():
            self.row += dlt_row
            self.col += dlt_col
            Karen.map[self.row][self.col] = self.symbol

    def put_beeper(self):
        row, col = self.row, self.col
        symbol = self.symbol
        if symbol in [">", "<"]:
            Karen.map[row][col] = "-"
        elif symbol in ["^", "v"]:
            Karen.map[row][col] = "|"

    def put_beeper_corner(self):
        row, col = self.row, self.col
        symbol = self.symbol
        Karen.map[row][col] = "+"    

    def print_map(self):
        for row in Karen.map:
            for item in row:
                print(item, end="")
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
        for row in Karen.map:
            beepers += row.count("X")
        return beepers
    
    def set_O(self, row, col):
        for i in range(len(Karen.map)):
            for j in range(len(Karen.map[0])):
                if Karen.map[i][j] == "8":
                    Karen.map[i][j] = "."
                           
        Karen.map[row][col] = "8"

def find_karen():
    map = get_map()
    symbols = [">", "v", "<", "^"]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in symbols:
                return i, j, map[i][j]

def verify_obs(karen):
    
    while True:
        karen.print_map()
        print(karen)
        try:
            if karen.if_front_is_clear() == True:
                karen.put_beeper()
                karen.move()
            elif karen.if_front_is_clear() == 'turn':
                karen.turn_right()
                karen.put_beeper_corner()
                karen.move()
            elif karen.if_front_is_clear() == '8':
                karen.turn_right()
                karen.put_beeper_corner()
                karen.move()
                karen.count_loop()
                print("loop count:" , karen.get_loop_count())
                if karen.get_loop_count() >= 2:
                    return True
                
        except IndexError:
            # print("beepers count:" ,karen.count_beepers())
            return False
    return False



def main():
    map = get_map()
    row, col, symbol = find_karen()
    karen = Karen(row, col, symbol)
    count = 0
    for i in range(10):
        for j in range(10):
            print("verify:", i , j)
            karen.set_O(i, j)
            if verify_obs(karen):
                count += 1
    print("valid obstacle count", count)

if __name__ == "__main__":
    main()
