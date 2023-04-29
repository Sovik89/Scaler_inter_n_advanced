import heapq

def solve(A):
        total=0
        if not A:
            return 0
        n=len(A)

        min_heap=[]
        for i in range(n):

            heapq.heappush(min_heap,A[i])
            
        #total=heapq.heappop(min_heap)
        
        while min_heap:
            first_val=heapq.heappop(min_heap)
            second_val=heapq.heappop(min_heap)
            temp_tot=first_val+second_val
            total+=(temp_tot)
            if min_heap:
                heapq.heappush(min_heap,temp_tot)

        return total
    
    
#print(solve([ 16, 7, 3, 5, 9, 8, 6, 15 ]))
print(solve([1, 2, 3, 4, 5]))