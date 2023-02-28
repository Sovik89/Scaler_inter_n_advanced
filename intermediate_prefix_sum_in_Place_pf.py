#Given an array A of N integers. Construct prefix sum of the array in the given array itself.


def solve(A):
    pf_sum=[]
    n = len(A)
    sum_val=0
    for i in range(n):
        sum_val+=A[i]
        pf_sum.append(sum_val)
    
    return pf_sum


#print(solve([1, 2, 3, 4, 5]))
print(solve([4, 3, 2]))
    