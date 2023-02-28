def solve(A):
    
    pos1=0
    
    pos2=len(A)-1
    
    while pos1<pos2:
        A[pos1],A[pos2]=A[pos2],A[pos1]
        
        pos1+=1
        pos2-=1
        
        
    return A



print(solve([1,2,3,4,5,6]))