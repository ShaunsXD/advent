def isValid(page):
    """
    check if page is valid
    bubble sort and go through each pair of numbers
    check if the pair is a valid rule in rules
    if valid pair, move on to the next pair
    if not valid pair, then return false

    :param page:
    :return:
    """
    rules = []
    first = []
    second = []
    # get rules in form of [a, b]
    with open("5_rules.txt", "r") as file:
        for line in file:
            line = line.strip()
            divide_idx = line.find("|")
            a = int(line[0:divide_idx])
            b = int(line[divide_idx + 1:])
            rules.append([a, b])
            first.append(a)
            second.append(b)
    valid = True
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            rule = [page[i], page[j]]
            if page[j] in second:
                if rule not in rules:
                    valid = False
            elif [page[j], page[i]] in rules:
                valid = False
    return valid


def part1():
    """
    Day 5 Part 1 for AOC24, prints the sum of middle index of valid pages

    :return:
    """
    sum = 0
    # get pages to be examined
    prints = []
    with open("5_print.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            prints.append([int(val) for val in line])

    for page in prints:
        if isValid(page):  # sum the middle index of only valid pages
            sum += page[len(page) // 2]

    print(sum)


def part2():
    """
    Day 5 Part 2 for AOC24, prints the sum of middle index of valid pages after swapping invalid pairs

    :return:
    """
    sum = 0
    rules = []
    with open("5_rules.txt", "r") as file:
        for line in file:
            line = line.strip()
            divide_idx = line.find("|")
            a = int(line[0:divide_idx])
            b = int(line[divide_idx + 1:])
            rules.append([a, b])

    prints = []
    with open("5_print.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            prints.append([int(val) for val in line])

    for page in prints:
        if not isValid(page):  # find invalid pages
            # bubble sort invalid pairs so they are valid
            for i in range(len(page)):
                for j in range(i + 1, len(page)):
                    if [page[j], page[i]] in rules:
                        page[j], page[i] = page[i], page[j]
            sum += page[len(page) // 2]

    print(sum)


if __name__ == "__main__":
    part1()
    part2()