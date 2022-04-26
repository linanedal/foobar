from fractions import Fraction
from fractions import gcd
import numpy as np

def todecimal(submatrix):

    rows = len(submatrix)
    columns = len(submatrix[0])

    for row in range(rows):
        rowdenom = float(sum(submatrix[row]))
        for cell in range(columns):
            decimalval = submatrix[row][cell] / rowdenom
            submatrix[row][cell] = decimalval

    return np.matrix(submatrix)

def toFraction(array):

    columns = len(array)

    for cell in range(columns):
        array[cell] = Fraction(array[cell]).limit_denominator()

    return array

def identity(dim):
    return np.identity(dim)

def lcm(list):

    def for2values(x,y):
        return abs(x*y) // gcd(x,y)

    import functools
    answer = functools.reduce(lambda x, y: for2values(x, y), list)

    return int(answer)

def solution(mat):

    if len(mat) == 1:
        return [1, 1]

# 1. identify the terminal states
    # how many rows and columns?
    rows = len(mat)
    columns = len(mat[0])
    # to determine which states are terminal:
    terminal = []
    nonterminal = []
    for row in range(rows):
        rowdenom = sum(mat[row])
        if rowdenom == 0:
            terminal.append(row)
        else:
            nonterminal.append(row)

    n = len(terminal)
    k = len(nonterminal)


# 2. put the matrix into standard form, find SUB1 and SUB2
    # create a (k x m) matrix where
    # sub1 and sub2 are contained
    lowermat = [] # (k x m)
    for row in nonterminal: # non-terminal states in the rows
        rowlist = []
        for tcol in terminal: # terminal states first
            rowlist.append(mat[row][tcol])
        for ncol in nonterminal: # non-terminal states second
            rowlist.append(mat[row][ncol])
        lowermat.append(rowlist)
    lowermat = todecimal(lowermat)

    sub1 = lowermat[:k, :n]
    sub2 = lowermat[:k, n:]

# 3. calculate the fundamental matrix (F = (I - SUB2)**-1)
    Ik = identity(k) # create a (k x k) identity matrix
    subtract = Ik - sub2
    fund = np.linalg.inv(subtract)

# 4. calculate F * SUB1
    fsub1 = np.dot(fund, sub1)

# 5. the first row (row 0) of F * SUB1 has our answers
    values = fsub1.tolist()[0]
    values = toFraction(values)

# 6. find the common denominator
    denoms = [val.denominator for val in values]
    commondenom = lcm(denoms)

# 7. create the result array
    results = []
    for val in values:
        denom = int(val.denominator)
        mul = int(commondenom/denom)
        numerator = int(val.numerator) * mul
        results.append(numerator)
    results.append(commondenom)

    return results


# test cases:
solution([[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])

solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])








#########################################################################

######### SET-UP #########

# suppose we have a matrix where

#     s0    s1   s2   s3
# s0   0   0.2  0.3  0.5
# s1   0    1    0    0
# s2   0    0    1    0
# s3  0.7  0.1  0.2   0


######### ID TERMINAL #########

# s1 and s2 are terminal
# s0 and s3 are non-terminal
# rearrange into standard form:

#     s1    s2   s0   s3
# s1   1    0    0    0
# s2   0    1    0    0
# s0  0.2  0.3   0   0.5
# s3  0.1  0.2  0.7   0


######### DECOMPOSE #########

# decompose into identity, zero, sub1, and sub2 matrix
# sub1 and sub2 will find the limiting matrix

# IDENTITY MATRIX -- len(terminal) x len(terminal) size
#    s1 s2
# s1 1  0
# s2 0  1

# ZERO MATRIX -- len(terminal) x len(non-terminal) size
#    s0 s3
# s1 0  0
# s2 0  0

# SUB1 MATRIX -- len(non-terminal) x len(terminal) size
# rows: non-terminal
# columns: terminal
#      s1   s2
# s0  0.2  0.3
# s3  0.1  0.2

# SUB2 MATRIX -- len(non-terminal) x len(non-terminal) size
# rows: non-terminal
# columns: non-terminal
#     s0   s3
# s0   0  0.5
# s3  0.7  0


######### SUMMARY SO FAR #########

# n: len(terminal)      (ie. # of terminal states)
# k: len(non-terminal)  (ie. # of non-terminal states)
# m: n + k              (ie. # of states)

# I -> (n x n)          # if we called the partitioned matrix A:
# Z -> (n x k)          # [   a11 = I      a12 = Z  ]
# SUB1 -> (k x n)       # [ a21 = SUB1   a22 = SUB2 ]
# SUB2 -> (k x k)

# [ (n x n)     (n x k) ]   # total rows: n + k = m
# [ (k x n)     (k x k) ]   # total columns: n + k = m

# total matrix: (m x m)


######### DERIVING THE FUNDAMENTAL MATRIX #########

# once the original matrix has been partitioned as such:
# [   I       Z  ]       # (ie. in standard form)
# [  SUB1   SUB2 ]

# then the matrix will approach a limiting matrix (call L), where
# L = [     I        Z  ]
#     [  F * SUB1    Z  ]

# F is called the fundamental matrix. F = (I - SUB2)**-1

# recall:
# I -> (n x n)
# SUB2 -> (k x k)

### ERROR!!! Don't they have to be the same size?
# YES, they do. So we need to make a (k x k) identity matrix (call Ik)
# ==> F = (Ik - SUB2)**-1           # F -> (k x k)

# thus L -> (m x m), since
# L = [     I - > (n x n)         Z -> (n x k)  ]
#     [  (F * SUB1) -> (k x n)    Z -> (k x k)  ]


######### PROPERTIES OF L #########

# 1. L[i, j] -> long-run prob. of going from state i to j.
# 2. Sum of entries in each row of F is the avg. number of rounds
# needed to go from each non-terminal state to terminal state.
