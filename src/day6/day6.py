def findGuard(arr):
    """
    Find the location of the guard on the grid
    :param arr:
    :return:
    """
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == '^' or arr[r][c] == 'v' or arr[r][c] == '<' or arr[r][c] == '>':
                return r, c


def countX(arr):
    """
    Count the cells containing X
    :param arr:
    :return:
    """
    count = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == "X":
                count += 1
    return count


def part1():
    """
    Day 6 Part 1 Prints Count of X after traversing path
    :return:
    """
    arr = []
    with open("6.txt", "r") as file:
        for l in file:
            line = []
            l = l.strip()
            for char in l:
                line.append(char)
            arr.append(line)

    r, c = findGuard(arr)
    dir = arr[r][c]

    while 0 <= r < len(arr) and 0 <= c < len(arr[0]):
        arr[r][c] = "X"
        if dir == "^":
            r -= 1
        elif dir == "v":
            r += 1
        elif dir == "<":
            c -= 1
        elif dir == ">":
            c += 1

        if r < 0 or r >= len(arr) or c < 0 or c >= len(arr[0]):
            break

        char = arr[r][c]
        if char == "#":
            if dir == "^":
                r += 1
                dir = ">"
            elif dir == "v":
                r -= 1
                dir = "<"
            elif dir == "<":
                c += 1
                dir = "^"
            elif dir == ">":
                c -= 1
                dir = "v"

    print(countX(arr))


def findCycle(arr):
    """
    very bad cycle finding algorithm
    :param arr:
    :return:
    """
    r, c = findGuard(arr)
    dir = arr[r][c]
    count = 0
    while 0 <= r < len(arr) and 0 <= c < len(arr[0]):
        count += 1
        if count >= 10000:
            return True

        arr[r][c] = "X"

        if dir == "^":
            arr[r][c] = "|"
        elif dir == ">":
            arr[r][c] = "-"
        elif dir == "v":
            arr[r][c] = "d"
        elif dir == "<":
            arr[r][c] = "l"

        if dir == "^":
            r -= 1
        elif dir == "v":
            r += 1
        elif dir == "<":
            c -= 1
        elif dir == ">":
            c += 1

        if r < 0 or r >= len(arr) or c < 0 or c >= len(arr[0]):
            break

        char = arr[r][c]
        if char == "|" and dir == "^":
            for l in arr:
                print("".join(l))
            return True
        if char == "-" and dir == ">":
            for l in arr:
                print("".join(l))
            return True
        if char == "d" and dir == "v":
            for l in arr:
                print("".join(l))
            return True
        if char == "l" and dir == "<":
            for l in arr:
                print("".join(l))
            return True

        if char == "#":
            if dir == "^":
                r += 1
                dir = ">"
            elif dir == "v":
                r -= 1
                dir = "<"
            elif dir == "<":
                c += 1
                dir = "^"
            elif dir == ">":
                c -= 1
                dir = "v"
    return False

def part2():
    """
    Day 6 Part 2, brute force every input with an obstacle and check if a cycle exists. Prints # of grids that give
    a cycle after adding # to cell.\
    :return:
    """
    arr = []
    cycles = 0
    with open("6.txt", "r") as file:
        for l in file:
            line = []
            l = l.strip()
            for char in l:
                line.append(char)
            arr.append(line)
    i = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            new_arr = [l[:] for l in arr]
            if new_arr[r][c] == ".":
                new_arr[r][c] = "#"
                i += 1
                #print(i)
                if findCycle(new_arr):
                    cycles += 1
    print(cycles)


if __name__ == "__main__":
    part1()
    part2()

