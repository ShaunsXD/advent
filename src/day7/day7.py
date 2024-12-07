import sys
sys.setrecursionlimit(10**6)


def part1():
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

    def dfs(target, num_list, result):
        if not num_list:
            if result == target:
                return True
            return False
        if result > target:
            return False

        if dfs(target, num_list[1:], result + num_list[0]):
            return True
        if dfs(target, num_list[1:], result * num_list[0]):
            return True
        return False

    for i in range(len(targets)):
        if dfs(targets[i], nums[i], 0):
            ans += targets[i]
            print(targets[i])
    print(ans)



def part2():
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

    def dfs(target, num_list, result):
        if not num_list:
            if result == target:
                return True
            return False
        if result > target:
            return False

        if dfs(target, num_list[1:], result + num_list[0]):
            return True
        if dfs(target, num_list[1:], result * num_list[0]):
            return True
        if dfs(target, num_list[1:], int(str(result) + str(num_list[0]))):
            return True


    for i in range(len(targets)):
        if dfs(targets[i], nums[i], 0):
            ans += targets[i]
            print(targets[i])
    print(ans)


if __name__ == "__main__":
    part1()
    part2()
