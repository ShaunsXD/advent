from matplotlib import pyplot as plt

def part1():
    with open("14.txt", "r") as file:
        data = file.read().strip().splitlines()

    arr = []
    for robot in data:
        temp = robot.split(" ")
        pos = temp[0].split(",")
        vel = temp[1].split(",")

        x = int(pos[0].split("=")[-1])
        y = int(pos[-1])

        vx = int(vel[0].split("=")[-1])
        vy = int(vel[-1])

        arr.append([(x, y), (vx, vy)])

    rows = 103
    cols = 101

    def print_grid(j):
        for robot in arr:
            x, y = robot[0]
            plt.scatter(x, cols - y)

        title = "iteration " + str(j) + ".png"
        plt.savefig(title)
        plt.clf()

    for j in range(100):
        for robot in arr:
            robot_x, robot_y = robot[0]
            robot_vx, robot_vy = robot[1]

            robot_x += robot_vx
            robot_y += robot_vy

            robot_x %= cols
            robot_y %= rows

            robot[0] = (robot_x, robot_y)

    mid_r = rows // 2
    mid_c = cols // 2

    quad1, quad2, quad3, quad4 = 0, 0, 0, 0

    for robot in arr:
        robot_x, robot_y = robot[0]
        if robot_x < mid_c and robot_y < mid_r:
            quad1 += 1
        elif robot_x > mid_c and robot_y < mid_r:
            quad2 += 1
        elif robot_x < mid_c and robot_y > mid_r:
            quad3 += 1
        elif robot_x > mid_c and robot_y > mid_r:
            quad4 += 1

    print(quad1 * quad2 * quad3 * quad4)



def part2():
    with open("14.txt", "r") as file:
        data = file.read().strip().splitlines()

    arr = []
    for robot in data:
        temp = robot.split(" ")
        pos = temp[0].split(",")
        vel = temp[1].split(",")

        x = int(pos[0].split("=")[-1])
        y = int(pos[-1])

        vx = int(vel[0].split("=")[-1])
        vy = int(vel[-1])

        arr.append([(x, y), (vx, vy)])

    rows = 103
    cols = 101

    def print_grid(j):
        do_print = True
        for val in dict.values():
            if val > 1:
                do_print = False
                break

        if do_print:
            for robot in arr:
                x, y = robot[0]
                plt.scatter(x, cols - y)

            title = "second " + str(j + 1) + ".png"
            plt.savefig(title)
            plt.clf()
            print("tree at second", j + 1)


    def countQuads():
        mid_r = rows // 2
        mid_c = cols // 2

        quad1, quad2, quad3, quad4 = 0, 0, 0, 0

        for robot in arr:
            robot_x, robot_y = robot[0]
            if robot_x < mid_c and robot_y < mid_r:
                quad1 += 1
            elif robot_x > mid_c and robot_y < mid_r:
                quad2 += 1
            elif robot_x < mid_c and robot_y > mid_r:
                quad3 += 1
            elif robot_x > mid_c and robot_y > mid_r:
                quad4 += 1

        return (quad1 * quad2 * quad3 * quad4)

    ans = []
    for j in range(rows * cols):
        dict = {}
        for robot in arr:
            robot_x, robot_y = robot[0]
            robot_vx, robot_vy = robot[1]

            robot_x += robot_vx
            robot_y += robot_vy

            robot_x %= cols
            robot_y %= rows

            robot[0] = (robot_x, robot_y)

            if (robot_x, robot_y) not in dict:
                dict[(robot_x, robot_y)] = 0
            dict[(robot_x, robot_y)] += 1
        print_grid(j)
        ans.append(countQuads())




if __name__ == "__main__":
    part1()
    part2()
