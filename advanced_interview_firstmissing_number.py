#Given an unsorted integer array, A of size N. Find the first missing positive integer.
class Solution:
    def firstMissingPositive(self,A):
            i=0
            N=len(A)
            # we irradicate the possibility of finding any natural number if 1 is itself not present
            isOnePresent=A.count(1)
            if isOnePresent==0:
                return 1
            
            while i < N:
                # if A[i] in goldilock zone or not        
                if A[i] > 0 and A[i] < N + 1:
                    correctindx = A[i] - 1
                    # not in position then swap
                    if A[correctindx] != A[i]:
                        A[i],A[correctindx] = A[correctindx],A[i]
                    else:
                        i+= 1

                else:
                    i +=1
            
            for i in range(N):
                if A[i]!=i+1:
                    return i+1
            return N+1
        
            
    