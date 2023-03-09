def check(n,A,B,M):
    count_val=1
    cows_placed=A[0]
    for i in range(1,n):
        if A[i]-cows_placed>=M:
            count_val+=1
            cows_placed=A[i]
            
            if count_val==B:
                return True
    return False

def solve(A, B):
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    #Approach
    # We’ll do the binary search to find the best possible maximum difference.

    # Since the maximum difference ranges between 0 to the max of array.
    # If we sort the array, the binary search starts with l = 0 and r = A[n-1], and we’ve to find the maximum distance.
    # For mid in binary search, we will check whether there are B stalls such that the minimum distance is greater than equal to mid.
    # Finally, store the maximum value we can get.
    A.sort()
    n=len(A)
    high=A[n-1]-A[0]
    low=1   
    ans=0
    
    while low<=high:
        mid=(low+high)>>1
        if check(n,A,B,mid):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    
    return ans

#print(solve([1, 2, 3, 4, 5],3))
print(solve([ 82, 61, 38, 88, 12, 7, 6, 12, 48, 8, 31, 90, 35, 5, 88, 2, 66, 19, 5, 96, 84, 95 ],8))
        
        
    