import heapq


def solve(A, B):
    
    min_heap=[]
    
    row,col=len(A),len(A[0])
    
    
    for i in range(row):
        for j in range(col):
            heapq.heappush(min_heap,A[i][j])
            
    
    for j in range(B-1):
        heapq.heappop(min_heap)
        
    x=heapq.heappop(min_heap)
    
    
    return x


print(solve(
    [  [5, 9, 11],
        [9, 11, 13],
        [10, 12, 15],
        [13, 14, 16],
        [16, 20, 21] ],12
))
    