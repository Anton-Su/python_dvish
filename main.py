import math


def main(z):
    if z < 31:
        return 32 * pow(z, 5) + 67
    if z < 78:
        return 1 + pow((12 * pow(z, 3) + 76), 3) + pow((36 * pow(z, 3)), 2)
    if z < 160:
        return 11 * 69 * pow(z, 2) - 25 * pow((pow(z, 2) / 61
                                               + 5 * pow(z, 3)), 6) - 1
    if z < 247:
        return pow((0.12 - z), 4) + 43 * pow((pow(z, 2)
                                              + 21 * z + pow(z, 3)), 2)
    return 1 - (pow(z, 3) / 93) - 23 * math.log10(z)


main(122)