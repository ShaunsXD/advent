import sys
sys.setrecursionlimit(10**6)

def printGrid(grid):
    for l in grid:
        print(l)


def findStart(arr):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == "S":
                return r, c


def findEnd(arr):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == "E":
                return r, c


grid = []
with open("20.txt", "r") as file:
    for l in file:
        line = []
        l = l.strip()
        for char in l:
            line.append(char)
        grid.append(line)

def gridToCost(grid, cost_grid):
    def fill(r, c, cost):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "#":
            return
        if cost >= cost_grid[r][c]:
            return
        cost_grid[r][c] = cost

        fill(r + 1, c, cost + 1)
        fill(r - 1, c, cost + 1)
        fill(r, c + 1, cost + 1)
        fill(r, c - 1, cost + 1)

    start_r, start_c = findStart(grid)
    fill(start_r, start_c, 0)
    return cost_grid


start_r, start_c = findStart(grid)
end_r, end_c = findEnd(grid)
cost_grid = gridToCost(grid, [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))])

saved = 0
saved_more = 0
for r1 in range(len(cost_grid)):
    for c1 in range(len(cost_grid[0])):
        if cost_grid[r1][c1] >= 999999999:
            continue
        for r2 in range(len(cost_grid)):
            for c2 in range(len(cost_grid[0])):
                if cost_grid[r2][c2] >= 999999999:
                    continue
                #print(r1, c1, saved)

                if r1 != r2 or c1 != c2:
                    if abs(r1 - r2) + abs(c1 - c2) == 2:
                        if cost_grid[r1][c1] - cost_grid[r2][c2] - 2 >= 100:
                            saved += 1
                    if abs(r1 - r2) + abs(c1 - c2) <= 20:
                        if cost_grid[r1][c1] - cost_grid[r2][c2] - abs(r1 - r2) - abs(c1 - c2) >= 100:
                            saved_more += 1

print(saved, saved_more)
