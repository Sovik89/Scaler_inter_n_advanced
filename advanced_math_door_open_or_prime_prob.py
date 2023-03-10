def solve(A):
    
    if A==1:
        return 1
    ans=1
    for i in range(2,A):
        square_val=i*i
        if square_val>A:
            break
        else:
            ans=i
        
    return ans
            
    
    
    

print(solve(10))
    
        