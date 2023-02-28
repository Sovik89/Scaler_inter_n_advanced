# Given an integer array A of size N. In one second, you can increase the value of one element by 1.
# Find the minimum time in seconds to make all elements of the array equal.

def solve(A):
    
    max_val=max(A)
    count_minutes=0
    
    for i in range(len(A)):
        count_minutes+=(max_val-A[i])
        
    return count_minutes


print(solve([2, 4, 1, 3, 2]))#O/P:8
    