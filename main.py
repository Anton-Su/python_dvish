bit_positions = {
    'C1': (0, 7),
    'C2': (7, 5),
    'C3': (12, 7),
    'C5': (21, 9)
    }


def main(spisok: list) -> int:
    binary_string = ['0'] * 30
    first, sec, third, fifth = spisok
    bin_value = bin(int(first[1]))[2:][::-1].ljust(7, '0')[-7:]
    binary_string[0:7] = bin_value
    bin_value = bin(int(sec[1]))[2:][::-1].ljust(5, '0')[-5:]
    binary_string[7:12] = bin_value
    bin_value = bin(int(third[1]))[2:][::-1].ljust(7, '0')[-7:]
    binary_string[12:19] = bin_value
    bin_value = bin(int(fifth[1]))[2:][::-1].ljust(9, '0')[-9:]
    binary_string[21:30] = bin_value
    return int(''.join(binary_string[::-1]), 2)



print(main(([('C1', '72'), ('C2', '17'), ('C3', '51'), ('C5', '508')])))



