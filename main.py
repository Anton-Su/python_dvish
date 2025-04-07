def main(data: list) -> list:
    cleaned = []
    for row in data:
        flag = '1' if row[1] == 'true' else '0'
        fio, raw_date = row[2].split('|')
        fio = fio.split(' ')[0]
        date = ('.'.join(raw_date.split('.')[::-1]).
                replace('.', '/'))
        cleaned.append([flag, fio, date])
    cleaned.sort(key=lambda x: (x[1]))
    result = list(map(list, zip(*cleaned)))
    return result



dannie = [[None, 'false', 'Домесук Захар|09.12.00'], [None, 'true', 'Водагли Арсен|02.12.03'], [None, 'true', 'Казугук Игнат|15.10.04'], [None, 'false', 'Гофов Самир|16.01.03']]
print(main(dannie))