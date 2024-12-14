def get_map():
    map_grid = []
    with open("data1.txt") as file:
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
            
map_grid = get_map()
x, y, symbol = (find_karel(map_grid))

# map_grid[x][y] = "."
# map_grid[45][8] = "^"
