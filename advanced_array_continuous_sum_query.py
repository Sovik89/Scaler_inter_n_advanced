# Problem Description
# There are A beggars sitting in a row outside a temple. 
# Each beggar initially has an empty pot. When the devotees come to the temple, 
# they donate some amount of coins to these beggars. Each devotee gives a fixed amount
# of coin(according to their faith and ability) to some K beggars sitting next to each other.

# Given the amount P donated by each devotee to the beggars ranging from 
# L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's 
# pot at the end of the day, provided they don't fill their pots by any other means.
# For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, Given by the 2D array B


def solve(A, B):
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    
    arr=[0]*A
    
    for b in B:
        L,R,P = b
        
        arr[L-1]+=P
        
        if R<A:
            arr[R]-=P
    
    sum =0
    for i in range(A):
        sum=sum+arr[i]
        arr[i]=sum
    
    return arr


print(solve(5,[[1, 2, 10], [2, 3, 20], [2, 5, 25]]))
        