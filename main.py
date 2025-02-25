from math import cos, tan, log

def main(y, x, z):
    first = pow(tan(pow(y, 3) + pow(z, 2)), 7) - pow(x, 2)
    sec = 97 * pow((50 * y + 10 * pow(y, 2) + pow(x, 3)), 2)
    third = 92 * pow(cos(z), 4)
    fourth = pow((52 + pow(y, 3) + 89 * pow(z, 2)), 3)
    fifth = 10 * pow(log(0.05 + pow(x, 2) / 38 + y, 2), 5)
    return first - ((sec - third) / (fourth - fifth))
