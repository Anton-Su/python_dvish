from math import atan


def main(n):
    if n == 0:
        return -0.24
    if n == 1:
        return 0.29
    else:
        return 34 * pow(atan(main(n-1)), 3) + main(n-2)

main(5)