def textToArr(filename):
    """
    Read a text file and return a list of lists
    :param filename:
    :return:
    """
    arr = []
    with open(filename, "r") as file:
        line = []
        for text in file:
            arr.append(text.strip().split())
    return arr


def part1():
    """
    Day 1 Part 1 for AOC24, prints the sum
    :return:
    """
    left = []
    right = []

    arr = textToArr(r"../1.txt")
    for line in arr:
        left.append(int(line[0]))
        right.append(int(line[1]))

    # sort arrs to match lowest with lowest
    left.sort()
    right.sort()
    sums = 0
    for i in range(len(left)):
        sums += abs(left[i] - right[i])

    print(sums)

def part2():
    """
    Day 1 Part 2 for AOC24, prints the similarity score
    :return:
    """
    right_dict = {}
    left = []
    right = []

    arr = textToArr(r"../1.txt")
    for line in arr:
        left.append(int(line[0]))
        right.append(int(line[1]))

    # sort arrs to match lowest with lowest
    left.sort()
    right.sort()
    # populate right dict with # of occurences
    for val in right:
        if val not in right_dict:
            right_dict[val] = 0
        right_dict[val] += 1

    sim_score = 0
    # check all vals in left and multiply by occurences in right
    for val in left:
        temp = 0
        if val in right_dict:
            temp = val * right_dict[val]
        sim_score += temp

    print(sim_score)


if __name__ == "__main__":
    part1()
    part2()
