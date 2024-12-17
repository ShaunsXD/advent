def part1():
    IR = 0
    A = 0
    B = 0
    C = 0
    outputs = []
    program = []

    with open("17.txt") as file:
        data = file.read().splitlines()
        A = int(data[0].split(" ")[-1])
        B = int(data[1].split(" ")[-1])
        C = int(data[2].split(" ")[-1])

        instructions = data[-1].split(" ")[-1].split(",")
        for instruction in instructions:
            program.append(int(instruction))

    def opcode_0(a, b):  # division and store in register A
        b = 2 ** b
        return a // b

    def opcode_1(a, b):  # bitwise XOR literal and store in register B
        return a ^ b

    def opcode_2(a):  # bst, combo operand mod 8 and store into B register
        return a % 8

    def opcode_3(a, b, IR):  # jump if not zero
        if a != 0:
            return b
        else:
            return IR + 2

    def opcode_4(b, c):  # bitwise XOR with register B and C
        return b ^ c

    def opcode_5(a):  # mod 8 then prints
        print(a % 8)
        outputs.append(a % 8)

    def opcode_6(a, b):  # same as opcode 0 but stores in register B
        b = 2 ** b
        return a // b

    def opcode_7(a, b):  # same as opcode 0 but stores in register C
        b = 2 ** b
        return a // b

    def operand(arg, a, b, c):
        if 0 <= arg <= 3:
            return arg
        elif arg == 4:
            return a
        elif arg == 5:
            return b
        elif arg == 6:
            return c

    print(program)
    while IR < len(program):
        opcode = program[IR]
        arg = operand(program[IR + 1], A, B, C)
        jumped = False

        if opcode == 0:
            A = opcode_0(A, arg)
        elif opcode == 1:
            B = opcode_1(B, program[IR + 1])
        elif opcode == 2:
            B = opcode_2(arg)
        elif opcode == 3:
            IR = opcode_3(A, program[IR + 1], IR)
            jumped = True

        elif opcode == 4:
            B = opcode_4(B, C)
        elif opcode == 5:
            opcode_5(arg)
        elif opcode == 6:
            B = opcode_6(A, arg)
        elif opcode == 7:
            C = opcode_7(A, arg)

        if not jumped:
            IR += 2

    print(outputs)


def part2(x):
    A = x
    B = 0
    C = 0
    arr = []
    while A != 0:
        B = A % 8
        B = B ^ 1
        C = A // (2 ** B)
        B = B ^ C
        B = B ^ 4
        #print(B % 8)
        arr.append(B % 8)

        A = A // (2 ** 3)
    return arr



def example(x):
    A = x
    B = 0
    C = 0
    arr = []
    while A != 0:
        A = A // 8
        #print(A % 8)
        arr.append(A%8)

    return arr

part2(0)

x = 1
match = -1
target_example = [0,3,5,4,3,0]
target = [2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0]
while x < 9999999999999999:
    print(x)
    #2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0
    arr = example(x)
    print(arr)
    if arr == target_example:
        print(x)
        break

    if arr[match:] == target_example[match:]:
        x *= 8
        match -= 1

    else:
        x += 1
