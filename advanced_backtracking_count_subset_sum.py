
#Non working code

def countsubsetsum(arr,n,i,sum,k):
    if i == n:
        if sum == k:
            return 1
        return 0
    
    #global count
    #take it
    
    sum+=arr[i]
    
    count+=countsubsetsum(arr,n,i+1,sum,k)
    
    
    #leave it
    
    sum-=arr[i]
    
    count+=countsubsetsum(arr,n,i+1,sum,k)
    
    return count


print(countsubsetsum([5,2,7],3,0,0,7,0))

#print(count)