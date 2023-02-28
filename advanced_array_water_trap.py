# Problem Description
# Given a vector A of non-negative integers representing an elevation map where 
# the width of each bar is 1, compute how much water it is able to trap after raining.

def trap(A):
    # @param A : tuple of integers
	# @return an integer
    n = len(A)
    pm = [0]*n #prefix max array
    sm = [0]*n #suffix max array
    total = 0
    pm[0] = A[0]
    sm[n-1] = A[n-1]
    for i in range(1,n):
        pm[i] = max(pm[i-1], A[i])
    for i in range(n-2, -1, -1):
        sm[i] = max(sm[i+1], A[i])
    for i in range(n):
        water_level=min(pm[i], sm[i])
        total +=  water_level- A[i]
    return total

#print(trap([0, 1, 0, 2]))
print(trap([1, 2]))



    
    