#same func for substrings in string, but let index increment by 1 instead
#will find overlapping substrings instead of skipping over the substring

def findAllOverlap(string, sub):
    """
    Find all occurences of a substring in a string with overlaps

    :param string:
    :param sub:
    :return:
    """
    i = 0
    idx = []
    while i < len(string):
        i = string.find(sub, i)
        if i == -1:
            return idx
        idx.append(i)
        i += 1
    return idx


def countXmas(line):
    """
    Count the number of XMAS in a line, forwards and backwards

    :param line:
    :return:
    """
    count = 0
    line = "".join(line)
    count += len(findAllOverlap(line, "XMAS"))
    count += len(findAllOverlap(line[::-1], "XMAS"))
    return count


def diagonalize(text):
    """
    Diagonalize traversal of a matrix
    https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/

    :param text:
    :return:
    """
    diag = []
    for line in range(1, (len(text) + len(text[0]))):
        temp = []
        start_col = max(0, line - len(text))
        counts = min(line, (len(text[0]) - start_col), len(text))
        for j in range(0, counts):
            temp.append(text[min(len(text), line) - j - 1][start_col + j])
        diag.append(temp)
    return diag


def part1():
    """
    Day 4 Part 1 for AOC24, prints the number of XMAS

    :return:
    """
    count = 0

    # want each char in text to be its own element to form nxn matrix
    text = []
    with open("4.txt", "r") as file:
        for row in file:
            temp = []
            row = row.strip()
            for char in str(row):
                temp.append(char)
            text.append(temp)

    # need to search 4 ways, rows, cols, top left diag, top right diag

    # row search
    for row in text:
        count += countXmas(row)

    # transpose matrix, then col search
    cols = [[text[r][c] for r in range(len(text))] for c in range(len(text[0]))]
    for col in cols:
        count += countXmas(col)

    # top left diag, then diag search
    diag1 = diagonalize(text)
    for diag in diag1:
        count += countXmas(diag)

    # reverse matrix for top right diag, then diag search
    text2 = [row[::-1] for row in text]
    diag2 = diagonalize(text2)

    for diag in diag2:
        count += countXmas(diag)

    print(count)

def countMas(line):
    """
    Count the number of MAS in a line, forwards and backwards

    :param line:
    :return:
    """
    count = 0
    line = "".join(line)
    count += len(findAllOverlap(line, "MAS"))
    count += len(findAllOverlap(line[::-1], "MAS"))
    return count

def part2():
    """
    Day 4 Part 2 for AOC24, prints the number of MAS

    :return:
    """
    count = 0
    text = []
    with open("4.txt", "r") as file:
        for row in file:
            temp = []
            row = row.strip()
            for char in str(row):
                temp.append(char)
            text.append(temp)

    # M.S
    # .A.
    # M.S

    # since diags share "A" in the center, search for "A"
    # if "A" found, get both diag strings
    # if both return a count for "MAS" then we have a match
    for r in range(len(text)):
        for c in range(len(text[0])):
            char = text[r][c]
            if char == "A":
                try:
                    diag1 = text[r - 1][c - 1] + char + text[r + 1][c + 1]
                    diag2 = text[r + 1][c - 1] + char + text[r - 1][c + 1]
                    if countMas(diag1) and countMas(diag2):
                        count += 1
                except:
                    continue
    print(count)


if __name__ == "__main__":
    part1()
    part2()
