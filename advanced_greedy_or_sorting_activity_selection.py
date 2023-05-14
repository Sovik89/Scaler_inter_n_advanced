import heapq

def solve(A, B):
    #A is the array of starting time
    #B is the list of ending time
    #we use a min_heap on the basis of tuple=(ending_time,starting_time)
    
    min_heap = []
    n=len(A)
    
    if n <= 1:
        return n
    
    for i in range(n):
        val = (B[i],A[i])        
        heapq.heappush(min_heap,val)
        
    starttime=0
    endtime=0
    count_of_work_spans=0
    
    while min_heap:
        work_item=heapq.heappop(min_heap)
        if work_item[1]>=endtime:
            count_of_work_spans+=1
            starttime=work_item[1]
            endtime=work_item[0]
            
    return count_of_work_spans


#print(solve([5, 1, 3, 0, 5, 8],[9, 2, 4, 6, 7, 9]))

print(solve([2,30,4,13,1,6,3,13],[40,49,11,30,37,23,30,37]))
            
    
        
    
    