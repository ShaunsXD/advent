def findTrailHead(arr):
    """
    Find the locations of the trailhead on the grid

    :param arr: grid to be searched
    :return: list of [r, c] coordinates of the trailheads
    :rtype: list
    """
    trailheads = []
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == 0:
                trailheads.append([r, c])
    return trailheads


def validDirection(arr, r, c):
    """
    Find a valid direction to move in the array

    :param arr: grid to be searched
    :param r: row index
    :param c: col index
    :return: 4 booleans indicating if the direction is valid
    """
    left, right, up, down = False, False, False, False
    if c - 1 >= 0 and arr[r][c - 1] - arr[r][c] == 1:
        left = True
    if c + 1 < len(arr[0]) and arr[r][c + 1] - arr[r][c] == 1:
        right = True
    if r - 1 >= 0 and arr[r - 1][c] - arr[r][c] == 1:
        up = True
    if r + 1 < len(arr) and arr[r + 1][c] - arr[r][c] == 1:
        down = True
    return left, right, up, down


def dfs(arr, r, c, total, visited=None):
    """
    simple dfs to find the number of paths from the trailhead to the end

    :param arr: grid to be searched
    :param r: row index
    :param c: col index
    :param total: total number of paths
    :param visited: set of visited coords
    :return: number of paths
    """
    directions = validDirection(arr, r, c)

    if isinstance(visited, set):
        if (r, c) in visited:
            return 0
        visited.add((r, c))

    if arr[r][c] == 9:
        return 1
    left, right, down, up = 0, 0, 0, 0
    if directions[0]:
        left = dfs(arr, r, c - 1, total, visited)
    if directions[1]:
        right = dfs(arr, r, c + 1, total, visited)
    if directions[2]:
        down = dfs(arr, r - 1, c, total, visited)
    if directions[3]:
        up = dfs(arr, r + 1, c, total, visited)
    return left + right + down + up


def part2(visited):
    """
    aoc day 10 part 1 and part 2

    :param visited: to use for part 1 where we look at unique coords
    :return:
    """
    arr = []
    with open("10.txt", "r") as file:
        for l in file:
            line = []
            l = l.strip()
            for char in l:
                line.append(int(char))
            arr.append(line)

    trailheads = findTrailHead(arr)
    sum = 0
    for trailhead in trailheads:
        sum += dfs(arr, trailhead[0], trailhead[1], total=0, visited=visited)
    print(sum)


if __name__ == "__main__":
    part2(visited=set())
    part2(visited=None)