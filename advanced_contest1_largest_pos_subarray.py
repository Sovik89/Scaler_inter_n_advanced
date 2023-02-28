def solve(A):
    #starting=0
    
    n=len(A)
    #ending=n
    output_arr=[]
    i=0
    
    #max_length=0
    temp_arr=[]   
    
    #max_length=len(temp_arr)
    while i< n:        
        if A[i]>0:
            temp_arr.append(A[i])
        else:
            if len(output_arr)<len(temp_arr):
                output_arr=temp_arr
            temp_arr=[]
                    #max_length=len(output_arr)
        i+=1
    if len(output_arr)<len(temp_arr):
        output_arr=temp_arr
        
    
    return output_arr  

#print(solve([5,6,-1,7,8]))
#print(solve([1,2,3,4,5,6]))      
print(solve([-5,-8,1,7,-1,11,-25,15,66,43])) 