#Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
import sys

def maxSubArray( A):
        sum = 0
        ans=-sys.maxsize

        for i in range(len(A)):
            sum+=A[i]
            ans=max(sum,ans)
            if sum <0:
                sum=0
            
        return ans