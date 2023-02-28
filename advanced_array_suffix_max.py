import sys

def solve(A):
        suffix_arr=[0]*len(A)
        max_val=-sys.maxsize
        n=len(A)
        for i in range(n-1,-1,-1):
            max_val=max(max_val,A[i])
            suffix_arr[i]=max_val

        return suffix_arr