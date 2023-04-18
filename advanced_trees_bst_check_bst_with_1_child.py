def solve( A):
        
        if A is None:
            return "YES"
        n=len(A)
        
        if n ==1:
            return "YES"
        
        #least unbreachable value
        lubv=float('-inf')
        #greatest unbreachable value
        gubv=float('inf')
        
        
        if A[0]>A[1]:
            gubv=A[0]
            
        else:
            lubv=A[0]
            
        
        
        for i in range(2,n):            
                if A[i]<lubv:
                    return "NO"
                if A[i]>gubv:
                    return "NO"
                if A[i]>A[i-1]:
                    lubv=A[i-1]
                else:
                    gubv=A[i-1]
               
                
        return "YES"
    
#print(solve([4,10,5,8]))
print(solve([ 44, 49, 42, 25, 2 ]))
#print(solve([12,1,9,6,2]))