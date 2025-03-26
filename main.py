bit_positions = {
    'C1': (0, 7),
    'C2': (7, 5),
    'C3': (12, 7),
    'C5': (21, 9)
    }


def main(spisok: list) -> int:
    binary_string = ['0'] * 30
    for name, value in spisok:
        start, length = bit_positions[name]
        bin_value = bin(int(value))[2:][::-1].ljust(length, '0')[-length:]
        binary_string[start:start + length] = bin_value  # Заменяем нужные биты в строке
    return int(''.join(binary_string[::-1]), 2)



print(main(([('C1', '72'), ('C2', '17'), ('C3', '51'), ('C5', '508')])))



