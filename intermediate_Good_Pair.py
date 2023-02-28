# Given an array A and an integer B. 
# A pair(i, j) in the array is a good pair if i != j and 
# (A[i] + A[j] == B). Check if any good pair exist or not.


def solve(A,K):
    
    n=len(A)
    
    for i in range(1,n):
        for j in range(0,i):
            if (A[i]+A[j])==K:
                return True
    
    return False


print(solve([1,2,3,4],7))#O/P: True

print(solve([1,2,4],4))#O/P: False

            