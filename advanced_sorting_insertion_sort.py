import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def insertion_sort(self,A,n):
        if n<=1:
            return
        self.insertion_sort(A,n-1)

        insertive_value=A[n-1]

        i=n-2

        while i>=0 and A[i]>insertive_value:
            A[i+1]=A[i]
            i-=1

        A[i+1]=insertive_value


    def solve(self, A):

        n=len(A)
        
        # for iterative steps only below will suffice

        # for i in range(1,n):
        #     for j in range(i-1,-1,-1):
        #         if A[j]>A[j+1]:
        #             A[j],A[j+1]=A[j+1],A[j]

        # return A

        #recursive step

        self.insertion_sort(A,n)

        return A
    



        
