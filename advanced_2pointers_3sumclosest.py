import sys

def threeSumClosest(A, B):
    
    A.sort()
    
    n=len(A)
    
    
    #ans=0
    min_diff= 100000007
    for i in range(n-2):
        j=i+1
        k=n-1
        while j<k:
            sum_val=A[i]+A[j]+A[k]            
            
            
            # temp=abs(sum_val-B)
            
            if sum_val==B:
                return sum_val
            if abs(min_diff-B)>abs(sum_val-B):
                    #min_diff = abs(temp - B)
                    min_diff = sum_val         
            
            elif sum_val<B:
                j+=1
            else:
                k-=1
      
    return min_diff


# print(threeSumClosest([-1, 2, 1, -4],1))
# print(threeSumClosest([1, 2, 3],6))
print(threeSumClosest([ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, 
                       -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3,
                       8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ],-1))    
        
                
                
                
    