#Reference: https://www.youtube.com/watch?v=U4UoR9vq238: Anuj Bhaiya solution
def solve(A, B):
    
    n=len(A)

    
    work_array=[[ 0 for i in range(3)] for j in range(n)]
    ans=[]
    
    #print(work_array)
    
    for i in range(n):
        work_array[i][0]=i+1
        work_array[i][1]=A[i]
        work_array[i][2]=B[i]
        
    print(work_array)
    
    work_array.sort(key=lambda x:x[2])
    
    fin_time = work_array[0][2]
    ans.append(work_array[0][0])
    
    for i in range(1,n):
        if work_array[i][1]>=fin_time:
            ans.append(work_array[i][0])
            fin_time=work_array[i][2]
            
    
    
    return(len(ans))
    
    
    
    

#print(solve([5, 1, 3, 0, 5, 8],[9, 2, 4, 6, 7, 9]))

print(solve([ 2, 30, 4, 13, 1, 6, 3, 13 ],[ 40, 49, 11, 30, 37, 23, 30, 37 ]))
     
     
    
    

