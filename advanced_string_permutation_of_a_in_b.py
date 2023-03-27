class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        n=len(A)
        m=len(B)
        count=0
        #len of A is less than len of B

        hash_map_A=dict()
        hash_map_B=dict()
        for i in range(n):
            if A[i] in hash_map_A:

                hash_map_A[A[i]]+=1
            else:
                hash_map_A[A[i]]=1
            if B[i] in hash_map_B:
                hash_map_B[B[i]]+=1
            else:
                hash_map_B[B[i]]=1
        
        if hash_map_A == hash_map_B:
            count+=1
        
        i=1
        for j in range(n,m):
            if B[j] in hash_map_B:
                hash_map_B[B[j]]+=1
            else:
                hash_map_B[B[j]]=1
            
            if hash_map_B[B[i-1]] > 1:
                hash_map_B[B[i-1]]-=1
            else:
                del hash_map_B[B[i-1]]
            
            if hash_map_A == hash_map_B:#compare function
                count+=1
            i+=1
        
        return count


