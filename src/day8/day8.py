def getAntennas():
    """
    Setup to get the antennas and the grid

    :return: Antennas dictionary and array grid
    """
    arr = []
    with open("8.txt", "r") as file:
        for l in file:
            line = []
            l = l.strip()
            for char in l:
                line.append(char)
            arr.append(line)

    antennas = {}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            char = arr[i][j]
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((i, j))
    return antennas, arr


def part1():
    """
    AOC Day 8 Part 1, colinear

    :return:
    """
    count = 0
    antennas, arr = getAntennas()
    for antenna in antennas:
        coords = antennas[antenna]
        for i in range(len(coords)):
            for j in range(len(coords)):
                if i != j:
                    a, b = coords[i], coords[j]
                    dX = a[0] - b[0]
                    dY = a[1] - b[1]
                    newX = a[0] + dX
                    newY = a[1] + dY
                    if 0 <= newX < len(arr) and 0 <= newY < len(arr[0]):
                        if arr[newX][newY] == "." or arr[newX][newY] != antenna or arr[newX][newY] != "#":
                            arr[newX][newY] = "#"

    for line in arr:
        for char in line:
            if char == "#":
                count += 1
    print(count)



def part2():
    """
    AOC Day 8 Part 2, spanning colinear antennas

    :return:
    """
    count = 0
    antennas, arr = getAntennas()

    for antenna in antennas:
        coords = antennas[antenna]
        for i in range(len(coords)):
            for j in range(len(coords)):
                if i != j:
                    a, b = coords[i], coords[j]
                    dX = a[0] - b[0]
                    dY = a[1] - b[1]
                    newX = a[0] + dX
                    newY = a[1] + dY
                    while 0 <= newX < len(arr) and 0 <= newY < len(arr[0]):
                        if arr[newX][newY] == "." or arr[newX][newY] != antenna or arr[newX][newY] != "#":
                            arr[newX][newY] = "#"
                        newX += dX
                        newY += dY

    for line in arr:
        for char in line:
            if char != ".":
                count += 1
    print(count)


if __name__ == "__main__":
    part1()
    part2()