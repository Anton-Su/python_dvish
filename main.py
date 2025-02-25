from math import log10


def main(a, b):
    result = 0
    for j in range(1, b + 1):
        for i in range(1, a + 1):
            result = result + (8 * pow(j, 5) + 98 *
                               pow(log10(i), 7) + 64 * pow(j, 4))
    for c in range(1, a + 1):
        result = result + pow(c, 5) + 6 * c
    return result

main(3, 4)