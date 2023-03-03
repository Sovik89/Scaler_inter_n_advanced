def searchMatrix(A, B):
    #Pseudo code:
    # N=len(row)

    # M=len(col)

    # Explaination:

    # low=0

    # high=N*M-1


    # mid = (low +high)//2


    # i should be mid/M  #more or less the row level should  be defined

    # j should be m%M    # residual element in the array(column value) is defined

    # if A[i][j]==target
    #     return true
    # if A[i][j]<target
    #     low=mid+1
    # if A[i][j]>target
    #     high=mid-1


    # iterate while low <= high
    
    N=len(A)
    M=len(A[0])
    
    low=0
    
    high=N*M-1
    
    while low<=high:
        
        mid= (low+high)//1#Similar to (low_high)//2
        
        i=mid//M
        j=mid%M
        x=A[i][j]
        if x==B:
            return 1
        if x>B:
            high=mid-1
            
        if x<B:
            low=mid+1
    
    return 0


print(searchMatrix([[1,3,5,7],[10, 11, 16, 20],[23, 30, 34, 50]],3))
        
        
    