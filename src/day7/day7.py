import sys
sys.setrecursionlimit(10**6)


def dfs(target, num_list, result, concat=False):
    """
    dfs to find if a set of operations exists to reach target with * + and ||

    :param target: target answer
    :param num_list: list of numbers to be operated on
    :param result: result of performing operations
    :param concat: boolean true or false to use || operator
    :return: whether the target can be reached with operators
    """
    if not num_list:
        if result == target:
            return True
        return False
    if result > target:
        return False

    if dfs(target, num_list[1:], result + num_list[0], concat):
        return True
    if dfs(target, num_list[1:], result * num_list[0], concat):
        return True
    if concat:
        if dfs(target, num_list[1:], int(str(result) + str(num_list[0])), concat):
            return True
    return False


def part2(concat=False):
    """
    AOC Day 8 Part 1 and Part 2, dfs to find valid set of operations to reach target

    :param concat: True if using concatenation operator
    :return:
    """
    with open("7.txt", "r") as file:
        data = file.read().splitlines()
    ans = 0
    targets = []
    nums = []
    for line in data:
        target = line[0:line.find(":")]
        targets.append(int(target))

        line = line[line.find(":") + 2:].split(" ")
        nums.append([int(val) for val in line])


    for i in range(len(targets)):
        if dfs(targets[i], nums[i], 0, concat):
            ans += targets[i]
    print(ans)


if __name__ == "__main__":
    part2(concat=False)
    part2(concat=True)
