def part1():
    count = 0
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

    for antenna in antennas:
        coords = antennas[antenna]
        print(antenna)
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
    count = 0
    arr = []
    with open("8.txt", "r") as file:
        for l in file:
            line = []
            empty_line = []
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
        print(line)
        print()
        for char in line:
            if char != ".":
                count += 1
    print(count)


part2()