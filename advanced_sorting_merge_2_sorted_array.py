class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):

        n=len(A)
        m=len(B)
        #C=[]---> Appending exceeds time limit, go for updation method
        C=[0]*(n+m)

        p1=0
        p2=0
        p3=0

        while p1<n and p2<m:
            if A[p1]<=B[p2]:
                C[p3]=A[p1]
                p1+=1
            else:#if I go for elif here time limit exceeds
                C[p3]=B[p2]
                p2+=1
            p3+=1
        
        while p1<n:
            C[p3]=A[p1]
            p1+=1
            p3+=1

        while p2<m:
            C[p3]=B[p2]
            p2+=1
            p3+=1

        return C


        
