def solve(A):
    
    A.sort()
    n=len(A)
    count=0
    # approach :
    # bruteforce - sort the array and check previous element in array is lesser or equal 
    # to current element , if so increment it till it becomes greater than previous element


    # optimized :
    #         the simple way to make the current element greater then previous element 
    # is just adding +1 to it ,and add that element to the current element . 
    # keep track of `count += A[i] - old_val`

    
    for i in range(1,n):
        if A[i]<=A[i-1]:
            temp=A[i]
            A[i]=A[i-1]+1
            count+=A[i]-temp
    return count