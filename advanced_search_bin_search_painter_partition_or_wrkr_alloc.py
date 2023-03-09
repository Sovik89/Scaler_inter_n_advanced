#Problem Description:

# Given 2 integers A and B and an array of integers C of size N. 
# Element C[i] represents the length of ith board.
# You have to paint all N boards [C0, C1, C2, C3 … CN-1]. 
# There are A painters available and each of them takes B units of time to paint 1 unit of the board.

# Calculate and return the minimum time required to paint all boards under 
# the constraints that any painter will only paint contiguous sections of the board.
# NOTE:
# 1. 2 painters cannot share a board to paint. That is to say, a board cannot be 
# painted partially by one painter, and partially by another.
# 2. A painter will only paint contiguous boards. This means a configuration where painter 
# 1 paints boards 1 and 3 but not 2 is invalid.

# Return the ans % 10000003.
def check(n,B,A,C,M):
    count_utilization=0
    summation_of_time=0
    
    for i in range(n):
        summation_of_time+=(C[i]*B)
        if summation_of_time>M:
            count_utilization+=1
            summation_of_time=C[i]*B
            if count_utilization==A:
                return False
    return True
    

def paint(A, B, C):
    # @param A : integer-->Number of painters available
	# @param B : integer-->time taken by each painter to paint a board
	# @param C : list of integers-->C[i] represents length of the ith board
	# @return an integer-->Return the ans % 10000003
    l=1
    h=0
    n=len(C)
    
    for i in range(n):
        h+=(C[i]*B)
        l=max(l,C[i]*B)
    
    ans=h
    
    #now we check with Binary Search
    
    while l<=h:
        mid=(l+h)//2
        
        if check(n,B,A,C,mid):
            ans=min(ans,mid)
            h=mid-1
        else:
            l=mid+1
    
    return ans % 10000003
 

#print(paint(10,1,[1,8,11,3]))
#print(paint(2,5,[1,10]))

    