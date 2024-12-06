def findGuard(arr):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == '^' or arr[r][c] == 'v' or arr[r][c] == '<' or arr[r][c] == '>':
                return r, c


def countX(arr):
    count = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == "X":
                count += 1
    return count


def part1():
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


if __name__ == "__main__":
    part1()



