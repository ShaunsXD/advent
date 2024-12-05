def doMul(text):
    """
    Multiply values in a string based on mul() format
    :param text:
    :return:
    """
    sums = 0
    splits = text.split("mul")
    for string in splits:
        if string[0] == "(":
            end_idx = string.find(")")
            if end_idx != -1:
                valid = True
                comma_idx = string.find(",")
                a = string[1:comma_idx]
                b = string[comma_idx + 1:end_idx]

                try:
                    val_a = int(a)
                    val_b = int(b)
                except:
                    valid = False

                if valid:
                    sums += val_a * val_b
    return sums


def findAll(string, sub):
    """
    Find all occurences of a substring in a string
    :param string:
    :param sub:
    :return:
    """
    i = 0
    idx = []
    while i < len(string):
        i = string.find(sub, i)
        if i == -1:  # no more substrings found so just return
            return idx
        idx.append(i)
        i += len(sub)
    return idx


def part1():
    """
    Day 3 Part 1 for AOC24, prints the sum
    :return:
    """
    sums = 0
    with open("3.txt", "r") as file:
        text = file.read()
    print(doMul(text))


def part2():
    """
    Day 3 Part 2 for AOC24, prints the sum
    :return:
    """
    with open("3.txt", "r") as file:
        text = file.read()

    # find idx of first substring occurence
    # add idx to list, skip to end of substring, loop

    # all idx of do() and don't()
    do_idx = findAll(text, "do()")
    dont_idx = findAll(text, "don't()")

    flag_do = True
    flag_dont = False
    text_modified = ""

    # check if current char is the start of a do() or don't()
    # update flags for which region we're in
    # if in a do() region, then append it to the modified text
    for i in range(len(text)):
        if i in do_idx:
            flag_do, flag_dont = True, False
        elif i in dont_idx:
            flag_dont, flag_do = True, False

        if flag_do:
            text_modified += text[i]

    print(doMul(text_modified))
