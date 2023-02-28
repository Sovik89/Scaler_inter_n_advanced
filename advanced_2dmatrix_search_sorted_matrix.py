import sys

def solve(A, B):
    
    n=len(A)
    m=len(A[0])
    
    i=0
    j=m-1
    
    value = 0
    ans=sys.maxsize 
    
    while (i<n) and (j>=0):
        if A[i][j] < B:
            i+=1
        elif A[i][j] > B:
            j-=1
        else:
            value+=1               
            ans=min(ans,((i+1)*1009+(j+1)))
            j-=1               
            
                
    if value>=1:        
        return ans
    else:
        return -1
    
    
#print(solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]],2))

print(solve([[1, 2],[3, 3]],3))
        
            
    

