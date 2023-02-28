# You are given an integer array A.
# You have to find the second largest element/value in the array 
# or report that no such element exists.
import sys

def solve(A):
    
    max_val=max(A)
    flag=0
    second_max_val=-sys.maxsize
    n=len(A)
    for i in range(n):
        if A[i] !=max_val:
            flag=1
            if A[i]>second_max_val:
                second_max_val=A[i]
                
    if flag ==0:
        return -1
    else:              
        return second_max_val


print(solve([2,1,2] ))




    
    