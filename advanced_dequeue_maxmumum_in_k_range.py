from collections import deque

def solve(A,B):
    n=len(A)
    
    if n==1:
        return A
    
    #for first iteration we do manual steps
    
    output_list=[]
    my_queue=deque()
    
    for i in range(B):
        
        
        if my_queue:
            while my_queue and my_queue[-1]< A[i] :
                my_queue.pop()
                
        my_queue.append(A[i])
                
    output_list.append(my_queue[0])
    
    if B==n:
        output_list
        
    for i in range(B,n):
        if my_queue[0]==A[i-B]:
            my_queue.popleft()
            
        if my_queue:
            while my_queue and my_queue[-1]<A[i]:
                my_queue.pop()
        my_queue.append(A[i])
        output_list.append(my_queue[0])
        
    
    return output_list

print(solve([1, 3, -1, -3, 5, 3, 6, 7],3))
    
                
                