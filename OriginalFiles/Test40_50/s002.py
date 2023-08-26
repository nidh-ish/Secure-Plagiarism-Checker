#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
    def __init__(self, m):
    # check if m is empty
    
    # check if all rows are lists      
    # check if all rows are non-empty lists    
    # check if all rows are of the same length
        pass
    # create matrix attribute using deep copy      
    # method matrix - to retur
    

def check_duplicates(A, p):
    if p >= len(A):
        return A[p]
    elif A[p+1] == A[p]:
        i = p-1
        while i >= 0 and A[i] == A[p]:
            i = i - 1
        return A[i]
    else:
        return A[p]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def random_partition(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)
