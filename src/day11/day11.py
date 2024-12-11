from collections import defaultdict


def blink(stones):
    """
    do 1 blink on the stones

    :param stones: dictionary of stones and count. ORDER DOESN'T MATTER LOL!!!!!!!
    :return:
    """
    stonedict = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            stonedict[1] += count
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])

            stonedict[left] += count
            stonedict[right] += count
        else:
            stonedict[2024 * int(stone)] += count
    return stonedict


def part2(iters):
    """
    AOC day 11 part 1 and part 2

    :param iters:
    :return:
    """
    stones = {}
    with open("11.txt", "r") as file:
        data = file.read().strip().split(" ")
        for stone in data:
            if stone in stones:
                stones[int(stone)] += 1
            else:
                stones[int(stone)] = 1

    for j in range(iters):
        stones = blink(stones)

    print(sum(stones.values()))


if __name__ == "__main__":
    part2(25)
    part2(75)

