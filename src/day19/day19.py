import functools


patterns = []
strings = []
with open("19.txt", "r") as file:
    data = file.read().split("\n\n")
    patterns = data[0].split(", ")
    strings = data[1].split("\n")

@functools.cache
def patternMatch(string):
    if not string:
        return 1
    count = 0
    for pattern in patterns:
        if string.startswith(pattern):
            count += patternMatch(string[len(pattern):])
    return count

possible = 0
count = 0
for string in strings:
    if patternMatch(string):
        possible += 1
    count += patternMatch(string)
print(possible, count)