import numpy as np


def weighted_sum_method(matritsa_kreteria, weights_kriteria):
    result = []
    for i in range(len(matritsa_kreteria)):
        result.append(sum([matritsa_kreteria[i][j] * weights_kriteria[j] for j in range(len(weights_kriteria))]))
    return rangirovanie(result)


def wikor_method(matritsa_kriteria, weights_kriteria, u):
    Q, S, R = [], [], []
    a = np.array(matritsa_kriteria).transpose()
    for i in range(len(matritsa_kriteria)):
        S_R_I = []
        for j in range(len(weights_kriteria)):
            maxi, mini = max(a[j]), min(a[j])
            S_R_I.append(weights_kriteria[j] * (maxi - matritsa_kriteria[i][j]) / (maxi - mini))
        S.append(sum(S_R_I))
        R.append(max(S_R_I))
    for i in range(len(S)):
        Q.append(u * ((S[i] - min(S)) / (max(S) - min(S))) + (1 - u) * ((R[i] - min(R)) / (max(R) - min(R))))
    return rangirovanie(Q, False)


def maut_method(matritsa_kriteria, weights_kriteria, utility_functions, step_size=1):
    X = np.copy(matritsa_kriteria)
    for i in range(0, X.shape[1]):
        if (utility_functions[i] == 'exp'):
            ArrExp = np.vectorize(u_exp)
            X[:, i] = ArrExp(X[:, i]) # к столбцу i применяется результат
        elif (utility_functions[i] == 'step'):
            ArrStep = np.vectorize(u_step)
            X[:, i] = ArrStep(X[:, i], step_size)
        elif (utility_functions[i] == 'quad'):
            ArrQuad = np.vectorize(u_quad)
            X[:, i] = ArrQuad(X[:, i])
        elif (utility_functions[i] == 'log'):
            ArrLog = np.vectorize(u_log)
            X[:, i] = ArrLog(X[:, i])
    for i in range(0, X.shape[1]):
        X[:, i] = X[:, i] * weights_kriteria[i]
    Y = np.sum(X, axis=1) # сумма по строкам
    return rangirovanie(Y.tolist())


def rangirovanie(result, reverse=True):
    for i in range(len(name_po)):
        result[i] = (result[i], name_po[i])
    result.sort(reverse=reverse)
    for i in range(len(result)):
        print(i + 1, result[i][1], f'({result[i][0]})')

def u_exp(x): # Function: небольшое увеличение сильно повышает полезность
    y = (np.exp(x ** 2) - 1) / 1.72
    return y

def u_step(x, op): # Function: Полезность изменяется дискретно
    y = np.ceil(op * x) / op
    return y

def u_log(x): # Function: прирост вначале значим, но затем эффект снижается.
    y = np.log10(9 * x + 1)
    return y

def u_quad(x): # Function: средние значения оптимальны, а крайние плохи.
    y = (2 * x - 1) ** 2
    return y

weights_kriteria = [0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
matritsa_kreteria = [
    [0.9, 0.85, 0.8, 0.8, 0.95, 0.5],
    [0.85, 0.8, 0.85, 0.85, 0.9, 0.8],
    [0.7, 0.9, 0.7, 0.9, 0.8, 0.7],
    [0.8, 0.75, 0.85, 0.75, 0.85, 0.95]
]
utility_functions = ['exp', 'exp', 'exp', 'exp', 'exp', 'step']
name_po = ['Recuva', 'EaseUS Data Recovery Wizard', 'R-Studio', 'Disk Drill']

def main():
    maut_method(matritsa_kreteria, weights_kriteria, utility_functions)
    print("--------------------")
    wikor_method(matritsa_kreteria, weights_kriteria, 0.5)
    print("--------------------")
    weighted_sum_method(matritsa_kreteria, weights_kriteria)
    print("--------------------")

main()
