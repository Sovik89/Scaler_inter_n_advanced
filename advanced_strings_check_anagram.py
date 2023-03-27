class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        # hashmap_A=dict()
        # hashmap_B=dict()
        if len(B)!=len(A):
            return 0
        n=len(A)
        
        # for i in range(n):
        #     if B[i] not in hashmap_B:
        #         hashmap_B[B[i]]=1
        #     else:
        #         hashmap_B[B[i]]=1
        #     if A[i] not in hashmap_A:
        #         hashmap_A[A[i]]=1
        #     else:
        #         hashmap_A[A[i]]=1
                
        
        # if hashmap_A == hashmap_B:
        #     return 1
        # else:
        #     return 0
        sum_ascii_A=0
        sum_ascii_B=0
        #for A
        for i in range(n):
            sum_ascii_A+=ord(A[i])
        
        #for B
        for i in range(n):
            sum_ascii_B+=ord(B[i])

        if sum_ascii_A == sum_ascii_B:
            return 1
        else:
            return 0