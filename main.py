from math import atan


def main(n):
    if n == 0:
        return -0.24
    elif n == 1:
        return 0.29
    f = [0.0] * (n + 1)
    f[0] = -0.24
    f[1] = 0.29
    for i in range(2, n + 1):
        f[i] = 34 * atan(f[i - 1]) ** 3 + f[i - 2]
    return f[n]

print(main(5))