s = ({'SAS', 1966, 1985},
     {'SAS', 1966, 1994},
     {'SAS', 1966, 1974, 'MQL4'},
     {'SAS', 1966, 1974, 'ASN.1'},
     {'SAS', 1959, 1985, 'RED'},
     {'SAS', 1959, 1985, 'PERL6'},
     {'SAS', 1959, 1994, 'RED'},
     {'SAS', 1959, 1994, 'PERL6'},
     {'SAS', 1959, 1974},
     {'X10', 1985},
     {'X10', 1994},
     {'X10', 1974},
     {'YACC'})


def main(r):
    s1 = set(r)
    return [i for i in range(len(s)) if not(len(s[i] - s1))][0]


print(main([1966, 'ASN.1', 1994, 'X10', 'PERL6']))