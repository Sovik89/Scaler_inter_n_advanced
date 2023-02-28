#Given an array A of N integers. Construct prefix sum of the array in the given array itself.
def solve(A):
    sum_val=0
    
    for i in range(len(A)):
        sum_val+=A[i]
        A[i]=sum_val
        
    return A


print(solve([1, 2, 3, 4, 5]))#O/P:[1, 3, 6, 10, 15]



