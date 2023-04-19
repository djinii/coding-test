def matrix_mult(A, B, mod):
    N = len(A)
    C = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= mod
    return C

def matrix_power(A, B, mod):
    N = len(A)
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    while B > 0:
        if B % 2 == 1:
            result = matrix_mult(result, A, mod)
        A = matrix_mult(A, A, mod)
        B //= 2
    return result

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = matrix_power(A, B, 1000)
for row in result:
    print(*row)