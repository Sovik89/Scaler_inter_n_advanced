# Given an integer array A containing N distinct integers.

# Find the number of unique pairs of integers in the array whose XOR is equal to B.

# NOTE:

# Pair (a, b) and (b, a) is considered to be the same and should be counted once.

def solve(A, B):
        
        distinct_integer=dict()
        n=len(A)
        count=0
        for i in range(n):
            #Proof:If, a XOR b = c, then a XOR c = b
            val=A[i]^B
            if val in distinct_integer:
                count+=1
            else:
                distinct_integer[A[i]]=i

        return count