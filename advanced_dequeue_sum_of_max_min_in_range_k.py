from collections import deque

def max_sum(arr,k):
    n=len(arr)
    
    
    
    #for first iteration we do manual steps
    
    ans=0
    my_queue=deque()
    
    for i in range(k):
        
        
        if my_queue:
            while my_queue and my_queue[-1]< arr[i] :
                my_queue.pop()
                
        my_queue.append(arr[i])
                
    ans+=my_queue[0]
    
    if k==n:
        ans
        
    for i in range(k,n):
        if my_queue[0]==arr[i-k]:
            my_queue.popleft()
            
        if my_queue:
            while my_queue and my_queue[-1]<arr[i]:
                my_queue.pop()
        my_queue.append(arr[i])
        ans+=my_queue[0]
        
    
    return ans

def min_sum(arr,k):
    n=len(arr)
    
    
    
    #for first iteration we do manual steps
    
    ans=0
    my_queue=deque()
    
    for i in range(k):
        
        
        if my_queue:
            while my_queue and my_queue[-1]> arr[i] :
                my_queue.pop()
                
        my_queue.append(arr[i])
                
    ans+=my_queue[0]
    
    if k==n:
        ans
        
    for i in range(k,n):
        if my_queue[0]==arr[i-k]:
            my_queue.popleft()
            
        if my_queue:
            while my_queue and my_queue[-1]>arr[i]:
                my_queue.pop()
        my_queue.append(arr[i])
        ans+=my_queue[0]
        
    
    return ans

def solve(A,B):
    mod_val=(10**9)+7
    min_val=min_sum(A,B)
    max_val=max_sum(A,B)
    
    return (min_val+max_val)%mod_val
    


print(solve([2, 5, -1, 7, -3, -1, -2],4))
        
        