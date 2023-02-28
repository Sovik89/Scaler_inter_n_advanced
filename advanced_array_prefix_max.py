import sys
#Problem Description

#Given an array A of length N, For every index i, you need to find the maximum value occurring in subarray from 0 to i.

def solve(A):

        max_val=-sys.maxsize
        for i in range(len(A)):
            max_val=max(max_val,A[i])
            A[i]=max_val
            
        return A
    

#print(solve([9, 7, 6, 18, 2]))
print(solve([16, 8, 24, 9, 25, 17]))