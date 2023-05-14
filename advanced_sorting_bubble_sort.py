class Solution:
    # @param A : list of integers
    # @return a list of integers
    def bubbleSort(self, A):
        n=len(A)
        for i in range(n):
            for j in range(1,n):
                if A[j-1]>A[j]:
                    A[j-1],A[j]=A[j],A[j-1]
        
        return A
                