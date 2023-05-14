class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()

        n=len(A)
        val=A[0]
        for i in range(n):
            if A[i]!=val:
                return 0
            val+=1
        
        return 1