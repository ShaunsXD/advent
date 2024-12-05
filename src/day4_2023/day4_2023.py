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


def part1():
    """
    Day 4 Part 1 for AOC24, prints the total score of cards
    :return:
    """
    # 2023 day 4
    total = 0
    text = textToArr("2023.txt")
    # go line by line (card by card) in text
    # split into left (winning) and right (card nums)
    for line in text:
        winning = []
        nums = []
        left = True
        count = 0
        for val in line:
            if val == "|":  # reached halfway point, next numbers are right arr (nums)
                left = False
            try:
                if left:
                    winning.append(int(val))
                else:
                    nums.append(int(val))
            except:
                continue
        # count how many card nums are in winning
        for num in nums:
            if num in winning:
                count += 1
        if count > 0:
            # get total score
            total += 2 ** (count - 1)

    print(total)


def part2():
    """
    Day 4 Part 2 for AOC24, prints the total dupes of cards
    :return:
    """
    text = textToArr("2023.txt")
    # default dict of all cards default 0 dupes
    cards_dict = dict.fromkeys([i for i in range(len(text))], 0)

    # go line by line (card by card) in text
    # split into left (winning) and right (card nums)
    for i in range(len(text)):
        line = text[i]
        winning = []
        nums = []
        left = True
        count = 0
        for val in line:
            if val == "|":
                left = False
            try:
                if left:
                    winning.append(int(val))
                else:
                    nums.append(int(val))
            except:
                continue

        for num in nums:
            if num in winning:
                count += 1

        # if winning card found, then add n (count + dupes) to count # of cards
        if count > 0:
            dupes = cards_dict[i]

            for j in range(count):
                try:  # make sure card # is valid
                    cards_dict[i + j + 1] += 1 + (1 * dupes)
                except:
                    break
    val = list(cards_dict.values())

    # ans is sum of all dupes + each original card
    print(sum(val) + len(text))


if __name__ == "__main__":
    part1()
    part2()
