


def main(H: set):
    E = set()
    alpha = set()
    for i in H:
        if 42 > i >= -48:
            E.add(i // 7 - 4 * i)
        peremenaya = 3 * i + i // 7
        if ((peremenaya >= 91 or peremenaya < 22) and
                (i >= 42 or i < -88)):
            alpha.add(abs(peremenaya))
    return len(E.union(alpha)) + sum(alpha)




print(main({96, 34, 35, -93, 9, 81, 52, 55, 92, 30}))