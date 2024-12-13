import numpy as np


def part1(do_offset=False):
    with open("13.txt.", "r") as file:
        data = file.read().split('\n\n')
        for i in range(len(data)):
            data[i] = data[i].split('\n')
    arr = []
    for i in range(len(data)):
        case = data[i]
        A = case[0]
        B = case[1]
        P = case[2]

        A = A.split('+')
        eq1 = (int(A[1].split(',')[0]), int(A[-1]))

        B = B.split('+')
        eq2 = (int(B[1].split(',')[0]), int(B[-1]))

        P = P.split('=')
        eq = (int(P[1].split(',')[0]), int(P[-1]))

        arr.append([eq1, eq2, eq])

    cost = 0
    for i in range(len(arr)):
        eq1, eq2, eq = arr[i]
        offset = 10000000000000 if do_offset else 0
        a = np.array([[eq1[0], eq2[0]], [eq1[1], eq2[1]]])
        b = np.array([eq[0] + offset, eq[1] + offset])
        x = np.round(np.linalg.solve(a, b))

        if (np.dot(a, x) == b).all():
            cost += 3 * x[0] + x[1]

    print(int(cost))


if __name__ == "__main__":
    np.set_printoptions(precision=30)
    part1()
    part1(do_offset=True)
