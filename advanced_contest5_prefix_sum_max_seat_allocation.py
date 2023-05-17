

def solve(A, B):
    n=len(A)
    ans=[0]*B
    
    for i in range(n):
               
        start=A[i][0]-1
        end=A[i][1]-1
        seats=A[i][2]
        
        ans[start]+=seats
              
        if end+1<B:
            ans[end+1]-=seats
            
    
    for i in range(1,B):
        ans[i]=ans[i-1]+ans[i]
        
    return ans          
    

print(solve([
    [1,2,10],
    [2,3,20],
    [2,5,25]
],5))