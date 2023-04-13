class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        i=0
        j=n-1
        sum_diagonal=0
        while i<n and j>=0:
            sum_diagonal+=A[i][j]
            i+=1
            j-=1

        return sum_diagonal
