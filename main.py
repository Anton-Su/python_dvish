dictionary = {}

def main(massiv: list) -> list:
    massiv = list(zip(*massiv))[1:]
    massiv = [list(i) for i in massiv]
    massiv[0] = [1 if massiv[0][i] == 'true' else 0
                 for i in range(len(massiv[0]))]
    sec = []
    for i in range(len(massiv[1])):
        rasdelenie = massiv[1][i].split('|')
        massiv[1][i] = rasdelenie[0].split(' ')[0]
        sec.append('.'.join(rasdelenie[1].split('.')[::-1]).
                   replace('.', '/'))
    massiv.append(sec)
    massiv = list(zip(*massiv))
    massiv = sorted(massiv, key=lambda x: (x[0], x[1]))
    return list(zip(*massiv))


dannie = [[None, 'true', 'Шицамяк Захар|17.04.00'], [None, 'true', 'Натий Демид|23.04.00'], [None, 'true', 'Фуфимиди Елисей|05.01.99'], [None, 'false', 'Зилолиди Иван|09.02.03']]
print(main(dannie))