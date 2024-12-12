#ORIGINAL ATTEMPT TO FIND SIDES OF A REGION

#want to take the perimeter of a region and bfs in 1 direction
#for every bfs, remove the perimeter from the region and sides++
#repeat until all sides are found
#needlessly complex and stupid approach just count the corners




# def moveDirection(coord, direction):
#     r, c = coord
#     if direction == "v":
#         return r + 1, c
#     elif direction == "^":
#         return r - 1, c
#     elif direction == ">":
#         return r, c + 1
#     elif direction == "<":
#         return r, c - 1
#
#
# def findDirection(coords, visited, r, c):
#     direction = ""
#     if (r + 1, c) in coords and (r + 1, c) not in visited:
#         direction = "v"
#     elif (r - 1, c) in coords and (r - 1, c) not in visited:
#         direction = "^"
#     elif (r, c + 1) in coords and (r, c + 1) not in visited:
#         direction = ">"
#     elif (r, c - 1) in coords and (r, c - 1) not in visited:
#         direction = "<"
#
#     return direction
# #
#
# def coordsToSides(coords):
#     if len(coords) == 1:
#         return 4
#
#     rectangle = True
#     first_r, first_c = coords[0]
#     for coord in coords:
#         if coord[0] != first_r:
#             rectangle = False
#             break
#
#     if rectangle:
#         return 4
#
#     rectangle = True
#     first_r, first_c = coords[0]
#     for coord in coords:
#         if coord[1] != first_c:
#             rectangle = False
#             break
#
#     if rectangle:
#         return 4
#
#     sides = 1
#     r, c = coords[0]
#
#     if (r, c) == (2, 3):
#         print()
#
#     start = coords[0]
#     visited = set()
#     dir = findDirection(coords, visited, r, c)
#     visited.add((r, c))
#     r, c = moveDirection((r, c), dir)
#
#     while len(visited) < len(coords):
#         new_dir = findDirection(coords, visited, r, c)
#         visited.add((r, c))
#         if new_dir != dir:
#             sides += 1
#         if new_dir == "":
#             break
#         r, c = moveDirection((r, c), new_dir)
#
#
#     return sides


# def coordsToSides(coords):
#     coords_dict = {}
#     for coord in coords:
#         if coord in coords_dict:
#             coords_dict[coord] += 1
#         else:
#             coords_dict[coord] = 1
#
#
#     counts = list(coords_dict.values())
#     dupes = 0
#     # while not all([count == 1 for count in counts]):
#     #     duped = False
#     #     for i in range(len(counts)):
#     #         count = counts[i]
#     #         if count > 1:
#     #             counts[i] -= 1
#     #             duped = True
#     #     if duped:
#     #         dupes += 1
#
#
#
#
#
#     #unique_coords = list(set(coords))
#     #unique_coords = coords
#     unique_coords = []
#     regions = 0
#
#     arr = [["." for i in range(10)] for j in range(10)]
#     for r in range(len(arr)):
#         for c in range(len(arr[0])):
#             while (r, c) in coords:
#                 arr[r][c] = "#"
#                 unique_coords.append((r, c))
#                 coords.remove((r, c))
#
#     while len(unique_coords) > 0:
#         coord = unique_coords.pop()
#         arr[coord[0]][coord[1]] = "."
#         printArr(arr)
#         traversed = False
#
#         if not traversed:
#             r, c = moveDirection(coord, "<")
#             while (r, c) in unique_coords:
#                 unique_coords.remove((r, c))
#                 arr[r][c] = "."
#                 printArr(arr)
#                 r, c = moveDirection((r, c), "<")
#                 traversed = True
#
#         if not traversed:
#             r, c = moveDirection(coord, ">")
#             while (r, c) in unique_coords:
#                 unique_coords.remove((r, c))
#                 arr[r][c] = "."
#                 printArr(arr)
#                 r, c = moveDirection((r, c), ">")
#                 traversed = True
#
#         if not traversed:
#             r, c = moveDirection(coord, "^")
#             while (r, c) in unique_coords:
#                 unique_coords.remove((r, c))
#                 arr[r][c] = "."
#                 printArr(arr)
#                 r, c = moveDirection((r, c), "^")
#                 traversed = True
#
#         if not traversed:
#             r, c = moveDirection(coord, "v")
#             while (r, c) in unique_coords:
#                 unique_coords.remove((r, c))
#                 arr[r][c] = "."
#                 printArr(arr)
#                 r, c = moveDirection((r, c), "v")
#                 traversed = True
#
#         regions += 1
#
#
#     return regions + dupes


def removeAreaToBlank(arr, blank, char, row, col):
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        return
    if arr[row][col] != char:
        return
    if blank[row][col] is not None:
        return

    blank[row][col] = char
    arr[row][col] = None
    removeAreaToBlank(arr, blank, char, row + 1, col)
    removeAreaToBlank(arr, blank, char, row - 1, col)
    removeAreaToBlank(arr, blank, char, row, col + 1)
    removeAreaToBlank(arr, blank, char, row, col - 1)

    return arr, blank


def regionFence(region, bulk=False):
    """
    fenced region is defined as a region that is surrounded by a blank space. dont actually need padding but makes
    visualization easier for me yeah
    counting perimeter is trivial, counting sides is the same is counting the number of corners in a region


    :param region: region of farmland
    :param bulk: whether to bulk together the sides of the region or not
    :return:
    """
    pad_region = [[None for i in range(len(region[0]) + 2)] for j in range(len(region) + 2)]
    for i in range(len(region)):
        for j in range(len(region[0])):
            pad_region[i + 1][j + 1] = region[i][j]

    perimeter_coords = []

    count, perimeter, corners = 0, 0, 0
    coords = []
    for i in range(len(pad_region)):
        for j in range(len(pad_region[0])):
            if not bulk:
                if pad_region[i][j] is not None:
                    count += 1
                    coords.append((i, j))
                    if pad_region[i + 1][j] is None:
                        perimeter += 1
                        perimeter_coords.append((i + 1, j))
                    if pad_region[i - 1][j] is None:
                        perimeter += 1
                        perimeter_coords.append((i - 1, j))
                    if pad_region[i][j + 1] is None:
                        perimeter += 1
                        perimeter_coords.append((i, j + 1))
                    if pad_region[i][j - 1] is None:
                        perimeter += 1
                        perimeter_coords.append((i, j - 1))
            else:
                if pad_region[i][j] is not None:
                    count += 1
                    coords.append((i, j))
                    if pad_region[i + 1][j] is None and pad_region[i][j + 1] is None:
                        corners += 1
                    if pad_region[i - 1][j] is None and pad_region[i][j + 1] is None:
                        corners += 1
                    if pad_region[i + 1][j] is None and pad_region[i][j - 1] is None:
                        corners += 1
                    if pad_region[i - 1][j] is None and pad_region[i][j - 1] is None:
                        corners += 1

                    if pad_region[i - 1][j] is not None and pad_region[i][j - 1] is not None and pad_region[i - 1][j - 1] is None:
                        corners += 1
                    if pad_region[i + 1][j] is not None and pad_region[i][j - 1] is not None and pad_region[i + 1][j - 1] is None:
                        corners += 1
                    if pad_region[i - 1][j] is not None and pad_region[i][j + 1] is not None and pad_region[i - 1][j + 1] is None:
                        corners += 1
                    if pad_region[i + 1][j] is not None and pad_region[i][j + 1] is not None and pad_region[i + 1][j + 1] is None:
                        corners += 1


    # for l in pad_region:
    #     a = ""
    #     for char in l:
    #         if not char:
    #             char = "."
    #         a += str(char)
    #     print(a)

    if not bulk:
        return count * perimeter
    else:
        return count * corners


def part1(bulk=False):
    """
    aoc part 1 and part 2 depending on bulk param

    :param bulk: whether to bulk together the sides of the region or not
    :return:
    """

    arr = []
    with open("12.txt", "r") as file:
        for l in file:
            line = []
            l = l.strip()
            for char in l:
                line.append(char)
            arr.append(line)

    cost = 0
    while arr != [[None for i in range(len(arr[0]))] for j in range(len(arr))]:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] is not None:
                    char = arr[i][j]
                    arr, blank_region = removeAreaToBlank(arr, [[None for i in range(len(arr[0]))] for j in range(len(arr))], arr[i][j], i, j)
                    cost += regionFence(blank_region, bulk=bulk)
                    break
    print(cost)



if __name__ == "__main__":
    part1(bulk=False)
    part1(bulk=True)
