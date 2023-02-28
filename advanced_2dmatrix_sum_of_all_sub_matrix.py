# Problem Description
# Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.

def solve(A):
    n=len(A)
    
    sums=0
    
    for j in range(n):
        for i in range(n):
            topleft=(i+1)*(j+1)
            bottomright=(n-i)*(n-j)
            sums+=topleft*bottomright*A[i][j]
            
    return sums