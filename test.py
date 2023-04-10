def maxSubarray(A, B, C):
    
    if A==1:
        return A[0]
    
    p1=0
    p2=1
    
    sum_val=C[p1]
    max_sum=0
    while p2!=A :
        
        
        if sum_val == B:
            return sum_val
        elif sum_val>B:
            sum_val-=C[p1]
            p1+=1
            if sum_val<B:
                max_sum=max(max_sum,sum_val)
        
        else:
            sum_val+=C[p2]
            p2+=1
            if sum_val<B:
                max_sum=max(max_sum,sum_val)
    
    if sum_val>B:
        while sum_val>B:
            sum_val-=C[p1]
            p1+=1
    max_sum=max(max_sum,sum_val)
             
        
        
    return max_sum


print(maxSubarray(5,12,[2,1,3,4,5]))
#print(maxSubarray(4,11,[7, 10, 3, 1]))       
    
    
