def selection_sort(A,k):  
    n = len(A) 
    if k>n-1:
        return -1 
      
    for i in range(n-1):  
        minIndex = i  
          
        for j in range(i+1, n):  
            if A[j]<A[minIndex]:  
                minIndex = j  
                  
        A[i], A[minIndex] = A[minIndex], A[i]  
          
          
    return A[k-1] 