import numpy as np

with open("25.txt", "r") as file:
    data = file.read().split("\n\n")

locks, keys = [], []

for x in data:
    x = x.split("\n")
    temp = []
    for row in x:
        temp.append(list(row))

    if temp[0][0] == "#":
        locks.append(temp)
    else:
        keys.append(temp)


def getLockHeights(lock):
    heights = []
    lock = lock[1:]
    for i in range(len(lock[0])):
        count = 0
        for j in range(len(lock)):
            if lock[j][i] == "#":
                count += 1
        heights.append(count)

    return heights


def getKeyHeights(key):
    heights = []
    key = key[:-1]
    for i in range(len(key[0])):
        count = 0
        for j in range(len(key)):
            if key[j][i] == "#":
                count += 1
        heights.append(count)

    return heights

count = 0
for lock in locks:
    for key in keys:
        lock_height = getLockHeights(lock)
        key_height = getKeyHeights(key)

        total_height = np.add(lock_height, key_height)
        if all(i <= 5 for i in total_height):
            count += 1
print(count)