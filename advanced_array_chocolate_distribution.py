import sys

def solve(A, B):
        # Sort the array.

        # Find the minimum difference between all subarrays of size B.
        if B == 0: return 0
        if not A: return 0
        A.sort()
        N = len(A)


        ans = sys.maxsize

        #sliding window
        for i in range(N-B+1):
            diff = A[i+B-1] - A[i]
            ans = min(ans,diff)
       
        return ans
    

print(solve([3, 4, 1, 9, 56, 7, 9, 12],5))