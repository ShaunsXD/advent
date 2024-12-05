def textToArr(file):
    """
    Convert text file to 2D array
    :param file:
    :return:
    """
    arr = []
    with open(file) as f:
        for text in f:
            arr.append(text.strip().split())
    return arr


def getDifferences(level):
    """
    Get differences between elements in a list
    :param level:
    :return:
    """
    differences = []
    for i in range(len(level) - 1):
        differences.append(level[i + 1] - level[i])
    return differences


def positive(differences):
    """
    Check if all values in a list are positive
    :param differences:
    :return:
    """
    return all(val > 0 for val in differences)


def negative(differences):
    """
    Check if all values in a list are negative
    :param differences:
    :return:
    """
    return all(val < 0 for val in differences)


def steps(differences):
    """
    Check if all values in a list are 1 or 3
    :param differences:
    :return:
    """
    return all(1 <= val <= 3 for val in differences)


def safeLevel(differences):
    """
    Check if a level is safe
    :param differences:
    :return:
    """
    if positive(differences) or negative(differences):
        differences = [abs(val) for val in differences]
        if steps(differences):
            return True
    return False


def part1():
    """
    Day 2 Part 1 for AOC24, prints the number of safe levels
    :return:
    """
    safe = 0
    arr = textToArr("2.txt")
    # go level by level
    # get differences between elements
    # check if all inc or dec
    # check if valid step length
    for line in arr:
        level = []
        for val in line:
            level.append(int(val))

        if safeLevel(getDifferences(level)):
            safe += 1

    print(safe)

def part2():
    """
    Day 2 Part 2 for AOC24, prints the number of safe levels after removing 1 element
    :return:
    """
    safe = 0
    arr = textToArr("2.txt")
    for line in arr:
        dampen = True
        level = []
        for val in line:
            level.append(int(val))

        if safeLevel(getDifferences(level)):
            safe += 1
            dampen = False  # unsafe level, try to remove 1 element until safe

        # same logic as pt. 1
        if dampen:
            damp_level = []
            for i in range(len(level)):
                # list comprehension to get new level without each index
                damp_level = [x for j, x in enumerate(level) if j != i]
                if safeLevel(getDifferences(damp_level)):
                    safe += 1
                    break

    print(safe)