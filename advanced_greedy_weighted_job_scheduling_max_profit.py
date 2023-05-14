import heapq

def solve(A):
    # A is a NX 3 list of starttime,endtime,profit
    
    min_heap=[]
    
    n=len(A)
    
    #heaping on end time
    for i in range(n):
        val=(A[i][1],A[i][0],A[i][2])        
        heapq.heappush(min_heap,val)
    
    prev_starttime=0
    prev_endtime=0
    prev_profit=0
    max_profit=0    
    
    while min_heap:
        current_endtime,current_starttime,current_profit=heapq.heappop(min_heap)
        #special case
        if current_endtime==current_starttime:
            max_profit+=current_profit
        
        elif current_endtime==prev_endtime:
            if current_starttime>prev_starttime and current_profit>prev_profit:
                max_profit-=prev_profit
                max_profit+=current_profit
        elif current_starttime>=prev_endtime:
            max_profit+=current_profit
            prev_profit=current_profit
            prev_starttime=current_starttime
            prev_endtime=current_endtime
        elif current_profit>max_profit:
            max_profit=current_profit
            prev_endtime=current_endtime
            prev_starttime=current_starttime
            prev_profit=current_profit      
        
            
    return max_profit
    



# print(solve([    
#     [1,2,50],
#     [3,5,20],
#     [6,9,100],
#     [2,100,200]
# ]))

print(solve([    
    [3,6,3],
    [6,7,8],
    [3,7,7],
    [3,10,9],
    [7,8,7],
    [6,6,3],
    [1,5,7],
    [2,5,1],
    [5,7,8]
]))


            
        
    