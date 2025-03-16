def x10(r):
    match r:
        case _ if 1985 in r:
            return 9
        case _ if 1994 in r:
            return 10
        case _ if 1974 in r:
            return 11


def fun_1994(r):
    match r:
        case _ if 'RED' in r:
            return 6
        case _ if 'PERL6' in r:
            return 7


def fun_1985(r):
    match r:
        case _ if 'RED' in r:
            return 4
        case _ if 'PERL6' in r:
            return 5


def f_1959(r):
    match r:
        case _ if 1985 in r:
            return fun_1985(r)
        case _ if 1994 in r:
            return fun_1994(r)
        case _ if 1974 in r:
            return 8


def f_1966(r):
    match r:
        case _ if 1985 in r:
            return 0
        case _ if 1994 in r:
            return 1
        case _ if 1974 in r:
            match r:
                case _ if 'MQL4' in r:
                    return 2
                case _ if 'ASN.1' in r:
                    return 3


def sas(r):
    match r:
        case _ if 1959 in r:
            return f_1959(r)
        case _ if 1966 in r:
            return f_1966(r)


def main(r):
    match r:
        case _ if 'SAS' in r:
            return sas(r)
        case _ if 'X10' in r:
            return x10(r)
        case _ if 'YACC' in r:
            return 12


print(main([1959, 'ASN.1', 1985, 'SAS', 'PERL6']))
