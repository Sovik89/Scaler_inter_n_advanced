import heapq

def solve(A, B, C):
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    
    #first max heap
    
    max_heap=[]
    min_heap=[]
    
    for i in range(B):
        max_val=-C[i]
        min_val=C[i]
        heapq.heappush(max_heap,max_val)
        heapq.heappush(min_heap,min_val)
        
    max_money=0
    min_money=0
    #pop out all the values as 
    max_A=min_A=A
    while max_A>0:
        #max_money
        if max_heap:
            max_popped_val=heapq.heappop(max_heap)
            max_operating_popped_val=-max_popped_val
            max_money+=(max_operating_popped_val)
            max_operating_popped_val-=1
            if max_operating_popped_val!=0:
                heapq.heappush(max_heap,-max_operating_popped_val)
        max_A-=1
    
    while min_A>0:
        
        #min_money
        if min_heap:
            min_popped_val=heapq.heappop(min_heap)
            #max_operating_popped_valmax_popped_val
            min_money+=(min_popped_val)
            min_popped_val-=1
            if min_popped_val!=0:
                heapq.heappush(min_heap,min_popped_val)
        
        min_A-=1
    
    return [max_money,min_money]


print(solve(4,3,[2,2,2]))
#print(solve(4,3,[2,1,1]))        
        
        