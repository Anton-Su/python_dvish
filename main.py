def x10(r):
    if 1985 in r:
        return 9
    if 1994 in r:
        return 10
    if 1974 in r:
        return 11


def fun_1994(r):
    if 'RED' in r:
        return 6
    if 'PERL6' in r:
        return 7


def fun_1985(r):
    if 'RED' in r:
        return 4
    if 'PERL6' in r:
        return 5


def f_1959(r):
    if 1985 in r:
        return fun_1985(r)
    if 1994 in r:
        return fun_1994(r)
    if 1974 in r:
        return 8


def f_1966(r):
    if 1985 in r:
        return 0
    if 1994 in r:
        return 1
    if 1974 in r:
        if 'MQL4' in r:
            return 2
        if 'ASN.1' in r:
            return 3


def sas(r):
    if 1959 in r:
        return f_1959(r)
    if 1966 in r:
        return f_1966(r)


def main(r):
    if 'SAS' in r:
        return sas(r)
    if 'X10' in r:
        return x10(r)
    if 'YACC' in r:
        return 12


print(main([1959, 'ASN.1', 1985, 'SAS', 'PERL6']))
