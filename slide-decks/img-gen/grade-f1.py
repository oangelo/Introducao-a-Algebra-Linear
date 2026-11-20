from fractions import Fraction as F

def rref(A, b):
    M = [[F(x) for x in A[i]] + [F(b[i])] for i in range(len(A))]
    m, n = len(M), len(A[0])
    piv = []
    r = 0
    for c in range(n):
        p = None
        for rr in range(r, m):
            if M[rr][c] != 0:
                p = rr
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for rr in range(m):
            if rr != r and M[rr][c] != 0:
                f = M[rr][c]
                M[rr] = [M[rr][k] - f * M[r][k] for k in range(n + 1)]
        piv.append(c)
        r += 1
        if r == m:
            break
    incons = any(all(M[i][c] == 0 for c in range(n)) and M[i][n] != 0 for i in range(m))
    if incons:
        return M, piv, 'INCONSISTENTE', None
    livres = [c for c in range(n) if c not in piv]
    if livres:
        return M, piv, 'INFINITAS (%d parametro(s))' % len(livres), livres
    sol = [None] * n
    for i, c in enumerate(piv):
        sol[c] = M[i][n]
    return M, piv, 'UNICA', sol

def show(nome, A, b, vars):
    M, piv, cls, extra = rref(A, b)
    print('==', nome, '| forma %dx%d' % (len(A), len(A[0])), '|', cls)
    for row in M:
        print('    ', ' '.join(str(x) for x in row))
    if cls == 'UNICA':
        print('     solucao:', ', '.join('%s=%s' % (v, extra[i]) for i, v in enumerate(vars)))
    elif cls.startswith('INFINITAS'):
        print('     colunas livres:', [vars[i] for i in extra])
    print()

show('A1 2x2 uma', [[2, 1], [1, -1]], [7, 2], 'xy')
show('A2 2x2 nenhuma', [[1, 1], [2, 2]], [3, 7], 'xy')
show('A3 2x2 infinitas', [[1, 1], [2, 2]], [3, 6], 'xy')
show('B1 3x3 sem troca', [[1, 1, 1], [2, -1, 1], [1, 2, -1]], [6, 3, 2], 'xyz')
show('B2 3x3 com troca', [[1, 1, 1], [1, -1, 1], [2, 1, -1]], [6, 2, 1], 'xyz')
show('B3 3x3 fracoes', [[2, 1, -1], [1, -1, 2], [3, 2, 1]], [1, 4, 5], 'xyz')
show('B4 3x3 dependente', [[1, 1, 1], [2, 2, 2], [1, -1, 0]], [3, 6, 0], 'xyz')
show('B5 3x3 homogeneo dep', [[1, 1, 1], [2, 2, 2], [1, -1, 0]], [0, 0, 0], 'xyz')
show('C1 2x3 mais incognitas', [[1, 1, 1], [1, -1, 1]], [4, 2], 'xyz')
show('C2 2x4', [[1, 1, 1, 1], [1, -1, 1, -1]], [4, 0], 'xyzw')
show('C3 3x2 mais equacoes', [[1, 1], [1, -1], [1, 1]], [2, 0, 5], 'xy')
show('C4 4x3 mais equacoes', [[1, 1, 1], [1, -1, 1], [2, 1, -1], [1, 0, 1]], [6, 2, 1, 3], 'xyz')
show('C5 2x3 livre no meio', [[1, 2, 3], [1, 2, 1]], [8, 4], 'xyz')
show('D1 4x4', [[1, 1, 1, 1], [0, 1, 2, 1], [0, 0, 1, 1], [0, 0, 0, 2]], [10, 8, 5, 6], 'xyzw')
show('D2 4x4 inconsistente', [[1, 1, 1, 1], [2, 2, 2, 2], [1, -1, 1, -1], [1, 0, 1, 1]], [4, 9, 0, 2], 'xyzw')

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print('== E1 (2x3)(3x2)')
A = [[1, 2, 0], [3, -1, 1]]
B = [[2, 1], [0, 3], [4, -2]]
print('    ', mul(A, B))
print('== E2 (3x2)(2x3)')
print('    ', mul(B, A))
print('== E3 AB x BA')
X = [[1, 1], [0, 1]]
Y = [[1, 0], [1, 1]]
print('     AB', mul(X, Y), ' BA', mul(Y, X))
