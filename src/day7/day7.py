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

    operators = ["+", "*"]

    for i in range(len(targets)):
        print(i)
        target = targets[i]
        num_list = nums[i]
        num_operations = len(num_list) - 1
        for j in range(2 ** num_operations):
            operations = []
            for k in range(num_operations):
                operations.append(operators[int(j / (2 ** k)) % 2])
            # print(operations)

            result = num_list[0]
            for k in range(num_operations):
                if operations[k] == "+":
                    result += num_list[k + 1]
                elif operations[k] == "*":
                    result *= num_list[k + 1]
                if result > target:
                    break

            if result == target:
                ans += target
                break
    print(ans)
