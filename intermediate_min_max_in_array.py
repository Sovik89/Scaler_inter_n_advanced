#Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.
import sys


def solve(A):
    
    min_val=sys.maxsize
    max_val=-sys.maxsize
    
    n=len(A)
    
    for i in range(n):
        if A[i]>max_val:
            max_val=A[i]
        if A[i]<min_val:
            min_val=A[i]
            
    return max_val+min_val


#print(solve([-2, 1, -4, 5, 3]))

#print(solve([1, 3, 4, 1]))
        
        