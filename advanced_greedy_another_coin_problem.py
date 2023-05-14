#import heapq

def solve(A):
    # @param A : integer
    # @return an integer
    
    #generate dynamic denomination
    
    max_denomination=1
    
    while max_denomination<A:        
        if max_denomination*5>=A:
            if max_denomination*5==A:
                max_denomination*=5
            break
        max_denomination*=5
    
    ans=0
    remaining_val=0
    
    while A>0:
        remaining_val=A%max_denomination
        ans+=(A//max_denomination)
        max_denomination//=5
        A=remaining_val
        
    return ans
    

print(solve(25))