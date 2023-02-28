# Given an array of integers A, find and return whether the given array contains 
# a non-empty subarray with a sum equal to 0.

# If the given array contains a sub-array with sum zero return 1, else return 0.


def solve(A):
    hashset=set()
    pf_array=[]
    sum=0
    for i in range(len(A)):
        sum+=A[i]
        pf_array.append(sum)
    
    hashset=set(pf_array)
    
    if 0 in hashset:
        return 1
    elif len(pf_array) != len(hashset):
        return 1
    else:
        return 0
    
    
print(solve([1, 2, 3, 4, 5]))
print(solve([1.-1]))
    
    
    