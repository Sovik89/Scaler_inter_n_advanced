def left_occurance(left,right,array,target):
    ans=-1
    while left<=right:
        mid=(left+right)//2        
        if array[mid]==target:
            ans=mid
            right=mid-1
        if array[mid]<target:
            left=mid+1
        if array[mid]>target:
            ans=mid
            right=mid-1
    
    return ans

def solve(A, B, C):
    
    #creating an array of 4 element with [0] values
    
    array=[0]*A
    output=[]
    for b in B:
        first,last=b
        
        array[first-1]+=1
        if A>last:
            array[last]-=1
        print(array)
    
    sum_val=0
    
    for i in range(A):
        sum_val+=array[i]
        array[i]=sum_val
    print(array)
    
    array.sort()
    
    for c in C:
        value=left_occurance(0,A-1,array,c)
        if value==-1:
            output.append(0)
        else:     
            count=A-left_occurance(0,A-1,array,c)           
            output.append(count)
    
    return output
        
    
    


print(solve(2,[[1,2],[1,2],[1,2],[1,2],[2,2]],[1,1,4,0,1]))    