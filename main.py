dictionary = {}

def main(data: list) -> list:
    cleaned = []
    for row in data:
        flag = 1 if row[1] == 'true' else 0
        fio, raw_date = row[2].split('|')
        fio = fio.split(' ')[0]  # Берем только первую часть ФИО
        date = ('.'.join(raw_date.split('.')[::-1]).
                replace('.', '/'))
        cleaned.append([flag, fio, date])
    cleaned.sort(key=lambda x: (x[0], x[1]))
    result = list(map(list, zip(*cleaned)))
    return result



dannie = [[None, 'true', 'Шицамяк Захар|17.04.00'], [None, 'true', 'Натий Демид|23.04.00'], [None, 'true', 'Фуфимиди Елисей|05.01.99'], [None, 'false', 'Зилолиди Иван|09.02.03']]
print(main(dannie))