from queue import Queue

def solve(A):
    my_queue=Queue(0)
    
    ans=""
    i=0
    my_queue.put("1")
    my_queue.put("2")
    
    while i<A:
        x=my_queue.get()
        
        my_queue.put(x+"1")
        my_queue.put(x+"2")
        
        i+=1
        ans=x+x[::-1]
        
    return ans
        
        
print(solve(4))    

#dry run: for 4 as input
# 1,2  11, 12,<--popped out, still in queue--> 21, 22 , 111 ,112 .121, 122

# Ans-->11   22   1111 1221