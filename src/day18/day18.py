grid = [["." for _ in range(71)] for _ in range(71)]


def dijkstra(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    dist = [[float("inf") for _ in range(m)] for _ in range(n)]
    dist[0][0] = 0
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        visited[y][x] = True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx] or grid[ny][nx] == "#":
                continue
            if dist[ny][nx] > dist[y][x] + 1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((nx, ny))
    return dist[-1][-1]

with open("18.txt", "r") as file:
    data = file.read().splitlines()
    for i, coords in enumerate(data):
        coord = coords.split(",")
        x, y = int(coord[0]), int(coord[1])
        #print(y, x)
        grid[y][x] = "#"

        if i == 1025:
            print(dijkstra(grid))

        if dijkstra(grid) > 99999999:
            print(y, x)
            break
