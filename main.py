from math import atan


def main(n):
    if n == 0:
        return -0.24
    if n == 1:
        return 0.29
    a, b = -0.24, 0.29
    for i in range(2, n + 1):
        c = 34 * pow(atan(b), 3) + a
        a, b = b, c
    return b


print(main(5))