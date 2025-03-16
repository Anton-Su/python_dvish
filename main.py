s = {
    0: {'SAS', 1966, 1985},
    1: {'SAS', 1966, 1994},
    2: {'SAS', 1966, 1974, 'MQL4'},
    3: {'SAS', 1966, 1974, 'ASN.1'},
    4: {'SAS', 1959, 1985, 'RED'},
    5: {'SAS', 1959, 1985, 'PERL6'},
    6: {'SAS', 1959, 1994, 'RED'},
    7: {'SAS', 1959, 1994, 'PERL6'},
    8: {'SAS', 1959, 1974},
    9: {'X10', 1985},
    10: {'X10', 1994},
    11: {'X10', 1974},
    12: {'YACC'}
}

def main(r):
    s1 = set(r)
    for key, value in s.items():
        if not (value - s1):
            return key

print(main([1959, 'ASN.1', 1994, 'YACC', 'PERL6']))