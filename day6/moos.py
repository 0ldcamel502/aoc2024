class Guard:
    def __init__(self, i, j, di, dj):
        self.i = i
        self.j = j
        self.di = di
        self.dj = dj

        self.i_start = self.i
        self.j_start = self.j
        self.di_start = self.di
        self.dj_start = self.dj
    
    def turn(self):
        self.di, self.dj = self.dj, -self.di

    def get_pos(self):
        return self.i, self.j
    
    def get_next_pos(self):
        return self.i+self.di, self.j+self.dj
    
    def move(self):
        self.i, self.j = self.get_next_pos()

    def get_direction(self):
        return self.di, self.dj

    def reset(self):
        self.i, self.j, self.di, self.dj = self.i_start, self.j_start, self.di_start, self.dj_start

    def __str__(self):
        return f"guard at: {self.get_pos()}, direction {self.di, self.dj}"
    
class Simulation:
    def __init__(self, n, m, obstacles, guard):
        self.n, self.m = n, m
        self.guard = guard
        self.visited = set()
        self.obstacles = obstacles

    def simulate(self):
        while True:
            i, j = self.guard.get_pos()
            di, dj = self.guard.get_direction()
            if (i, j, di, dj) in self.visited:
                return True
            if i<0 or i>=self.n or j<0 or j>=self.m:
                return False
            self.visited.add((i, j, di, dj))
            ii, jj = self.guard.get_next_pos()
            while (ii, jj) in self.obstacles:
                self.guard.turn()
                ii, jj = self.guard.get_next_pos()
            self.guard.move()
            
def part1(obstacles, guard):
    n, m = len(grid), len(grid[0])
    sim = Simulation(n, m, obstacles, guard)
    sim.simulate()
    visited_sim = set()
    for i, j, _, _ in sim.visited:
        visited_sim.add((i, j))
    return visited_sim

def part2(grid, obstacles, guard, tovisit):
    res = 0
    n, m = len(grid), len(grid[0])
    for i, j in tovisit:
        char = grid[i][j]
        if char==".":
            obstacles.add((i, j))
            guard.reset()
            sim = Simulation(n, m, obstacles, guard)
            if sim.simulate():
                res+=1
                print(res, i, j)
                with open("outputmoos.txt", "a") as output:
                    output.write(f'{res}, {i}, {j}\n')
            obstacles.remove((i, j))
    print(res)

fname = "data.txt"
with open(fname) as inputfile:
    grid = inputfile.read().split()
obstacles = set()
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char=="#":
            obstacles.add((i, j))
        if char=="v":
            guard = Guard(i, j, 1, 0)
        if char=="^":
            guard = Guard(i, j, -1, 0)
        if char=="<":
            guard = Guard(i, j, 0, -1)
        if char==">":
            guard = Guard(i, j, 0, 1)
tovisit = part1(obstacles, guard)
print(len(tovisit))
guard.reset()
part2(grid, obstacles, guard, tovisit)