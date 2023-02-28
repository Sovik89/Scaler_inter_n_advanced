def solve(A,B):
    #rotation from 0 to n
    pos1=0    
    pos2=len(A)-1
    
    while pos1<pos2:
        A[pos1],A[pos2]=A[pos2],A[pos1]
        
        pos1+=1
        pos2-=1
    
    #rotation from 0 to B-1
    pos1=0
    actual_rotation=B%len(A)
    pos2=actual_rotation-1
    while pos1<pos2:
        A[pos1],A[pos2]=A[pos2],A[pos1]        
        pos1+=1
        pos2-=1
        
    # rotation from B to n-1
    pos1=actual_rotation
    pos2=len(A)-1
    while pos1<pos2:
        A[pos1],A[pos2]=A[pos2],A[pos1]        
        pos1+=1
        pos2-=1
        
    return A



print(solve([1, 2, 3, 4],2))#O/P: 3,4,1,2