def solve(A,B,C):
    n = len(A)
    
    sum_1=0
    sum_0=0
    max_sum=0
    for i in range(n):
        # We are taking the sum for A[i] where B[i]=1, This is always getiing added in sum_1 and sum_0 is getting
        # added by A[i] where B[i] =0
        # now we are taking a window of C when value of sum_0 with the B[i] for upcoming value where B[i] =0
        sum_1+=(B[i]*A[i])
        sum_0+=((1-B[i])*A[i])
        if i >=C:
            sum_0-=(1-B[i-C])*A[i-C]
        max_sum=max(max_sum,sum_0)
            
    return max_sum+sum_1
        
         
    
    
    
    
 
 
# print(solve([1,4,2,8],[0,0,0,1],2)) 
print(solve([2,1,4],[0,0,1],1))  


# A=[1,4,2,8]
# B=[0,0,0,1]

# C=2       
            
        
            