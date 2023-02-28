#Given an array A of N integers. Count the number of elements that have at least 1 elements greater than itself.


def solve(A):
    max_ele=A[0]
    count_ele=0
    n=len(A)
    for i in range(1,n):
        if max_ele < A[i]:
            max_ele=A[i]
    
    for i in range(n):
        if max_ele != A[i]:
            count_ele+=1
            
    return count_ele


#print(solve([5, 5, 3]))#OP:1
#print(solve([3, 1, 2]))#OP:2