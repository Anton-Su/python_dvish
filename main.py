bit_positions = {
    'C1': (0, 7),
    'C2': (7, 5),
    'C3': (12, 7),
    'C5': (21, 9)
    }


def main(spisok: list) -> int:
    result = 0
    for name, value in spisok:
        shift, size = bit_positions[name]
        maska = (1 << size) - 1
        chiclo = (int(value) & maska) << shift
        result |= chiclo
    return result