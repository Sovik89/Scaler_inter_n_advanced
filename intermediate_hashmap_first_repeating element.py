# Given an integer array A of size N, find the first repeating element in it.
# We need to find the element that occurs more than once and whose index of 
# the first occurrence is the smallest.

# If there is no repeating element, return -1.

def solve(A):
    freq_dict={}
    
    for i in range(len(A)):
        if A[i] not in freq_dict:
            freq_dict[A[i]]=1
        else:
            freq_dict[A[i]]+=1
            
    for i in range(len(A)):
        if freq_dict[A[i]]>1:
           return A[i]
    
    return -1


print(solve([6, 10, 5, 4, 9, 120])) # -1

print(solve([10, 5, 3, 4, 3, 5, 6]))# 5