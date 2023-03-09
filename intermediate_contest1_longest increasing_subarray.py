def solve(A):
    #sliding window
    n=len(A)
    if n ==1:
        return 1
    
            
    i=0
    ans=0
    while i<n:
        j=i+1
        
        while j<n and A[j]>A[j-1]:
            j+=1
        ans=max(ans,j-i)
        i=j
    
    return ans
            
    

#print(solve([2,1,3,4]))
print(solve([6,9,9,8]))
#print(solve([16,3,3,6,7,8,17,13,7]))
#print(solve([10,9,18]))
#print(solve([7,11]))
    
    
    
    
    
        
            