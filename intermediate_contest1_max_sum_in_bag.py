def solve(A,B,C):
    output_list=[]
    n=len(B)
    
    for i in range(n):
        if B[i]==1:
            output_list.append(A[i])
            
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    j=0
    i=0
    while j <=C:
        if B[i]==0:
            output_list.append(A[i])
            j+=1
        i+=1
    
    sum_val=0
    
    for i in range(len(output_list)):
        sum_val+=output_list[i]
    
        
    return sum_val        
            
        
            