def part1():
    disk = []
    new_disk = []
    id = 0
    with open("9.txt", "r") as file:
        line = file.readline().strip()
        for char in line:
            disk.append(int(char))

    for i in range(len(disk)):
        if i % 2 == 0:
            for i in range(disk[i]):
                new_disk.append(id)
            id += 1
        else:
            for i in range(disk[i]):
                new_disk.append(".")

    print(new_disk)

    while "." in new_disk:
        char = new_disk[-1]
        if char == ".":
            new_disk.pop()
        else:
            free_idx = new_disk.index(".")
            new_disk[free_idx] = new_disk.pop()

    id = 0
    sum = 0
    for char in new_disk:
        if char != ".":
            sum += id * int(char)
            id += 1
    print(sum)


def part2():
    disk = []
    new_disk = []

    free_list = []
    alloc_list = []

    id = 0
    with open("9.txt", "r") as file:
        line = file.readline().strip()
        for char in line:
            disk.append(int(char))

    for i in range(len(disk)):
        if i % 2 == 0:
            alloc_list.append([disk[i], len(new_disk)])
            for i in range(disk[i]):
                new_disk.append(id)
            id += 1
        else:
            free_list.append([disk[i], len(new_disk)])
            for i in range(disk[i]):
                new_disk.append(".")

    #alloc list format, list of allocated space, [length of space, start index]
    #free list format, list of free space, [length of space, start index]
    print(alloc_list)
    print(free_list)
    print(new_disk)

    #malloc and free list approach
    #go reverse order of all allocated data, and then check the free list to see if there's a valid free block
    #valid free block means that the size of the free block <= size of alloc block, and idx of free block <= idx of alloc block
    #swap the data of the free block with the alloc block and update the free block size and index or pop
    #break if the alloc block is allocated
    #loop
    for i in range(len(alloc_list) - 1, -1, -1):
        block = alloc_list[i]
        size, idx = block[0], block[1]

        for i in range(len(free_list)):
            free_block = free_list[i]
            free_size, free_idx = free_block[0], free_block[1]
            #check for valid free block
            if size <= free_size and free_idx <= idx:
                for j in range(size):
                    new_disk[free_idx], new_disk[idx + j] = new_disk[idx + j], new_disk[free_idx]
                    free_size -= 1
                    free_idx += 1

                if free_size == 0:
                    free_list.pop(i)
                else:
                    free_list[i][0] = free_size
                    free_list[i][1] = free_idx
                break
    sum = 0
    for i in range(len(new_disk)):
        if new_disk[i] != ".":
            sum += i * new_disk[i]
    print(new_disk)
    print(sum)



part1()
part2()