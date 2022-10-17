import math

"""

operations on matrices

"""

def sum(A, B):
    """sum of two matrix"""
    len_i_A = len(A)
    len_j_A = len(A[0])
    len_i_B = len(B)
    len_j_B = len(B[0])
    C = [[]]
    if len_j_A != len_j_B or len_i_A != len_i_B:
        print("Error")
    else:
        C = [[A[i][j] + B[i][j] for j in range(len_j_A)] for i in range(len_i_A)]
    return C


def subtract(A, B):
    """subtract of two matrix"""
    len_i_A = len(A)  # row of matrix A
    len_j_A = len(A[0])  # column of matrix A
    len_i_B = len(B)  # row of matrix B
    len_j_B = len(B[0])  # column of matrix A
    C = [[]]
    if len_j_A != len_j_B or len_i_A != len_i_B:
        print("Error")
    else:
        C = [[A[i][j] - B[i][j] for j in range(len_j_A)] for i in range(len_i_A)]
    return C


def mult(A, B):
    """multiplication of two matrix"""
    len_i_A = len(A)  # row of matrix A
    len_j_A = len(A[0])  # column of matrix A
    len_i_B = len(B)  # row of matrix B
    len_j_B = len(B[0])  # column of matrix A
    if len_j_A == len_i_B:
        C = [[0 for j in range(len_j_B)] for i in range(len_i_A)]
        for i in range(len_i_A):
            for j in range(len_j_B):
                for k in range(len_j_A):
                    C[i][j] += A[i][k] * B[k][j]
    else:
        C = [[]]
        print('Incorrect dimension')
        print(f"B_i={len_i_B}; A_j={len_j_A}")
    return C


def transp(A):
    """matrix transposition"""
    len_j = len(A[0])
    len_i = len(A)
    C = [[A[i][j] for i in range(len_i)] for j in range(len_j)]
    return C


def norm1(A):
    """matrix norm 1"""
    len_j = len(A[0])
    len_i = len(A)
    max = 0
    sum = 0
    for i in range(len_i):
        for j in range(len_j):
            sum += abs(A[i][j])
        if (sum > max):
            max = sum
        sum = 0
    return max


def norm3(A):
    """matrix norm 3"""
    len_j = len(A[0])
    len_i = len(A)
    max = 0
    sum = 0
    for j in range(len_j):
        for i in range(len_i):
            sum += abs(A[i][j])
        if (sum > max):
            max = sum
        sum = 0

    return max


def norm_frob(A):
    """Frobenius matrix norm """
    len_j = len(A[0])
    len_i = len(A)
    sum = 0
    for i in range(len_i):
        for j in range(len_j):
            sum += pow(A[i][j], 2)
    return math.sqrt(sum)


def min_norm(A):
    return min(norm1(A), norm3(A), norm_frob(A))


def check_diag(A):
    """check matrix for diagonal dominance"""
    flag = True
    n = len(A)
    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j:
                sum += abs(A[i][j])
        if abs(A[i][i]) - sum <= 0:
            flag = False
    return flag


def diagon_dom(A):
    """finding diagonal dominance"""
    fl = True
    diag_dom = A[0][0];
    for i in range(len(A)):
        var = 0;
        for j in range(len(A)):
            if i == j:
                continue
            var += abs(A[i][j])
        if abs(A[i][i]) - var <= 0:
            return -1
        else:
            if A[i][i] - var < diag_dom:
                diag_dom = A[i][i] - var
    return diag_dom
