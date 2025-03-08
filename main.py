


def main(H: set):
    E = {i // 7 - 4 * i for i in H if 42 > i >= -48}
    X = {3 * i + i // 7 for i in H if i >= 42 or i < -88}
    alpha = {abs(i) for i in X if i >= 91 or i < 22}
    return len(E | alpha) + sum(alpha)




print(main({96, 34, 35, -93, 9, 81, 52, 55, 92, 30}))