import heapq


def k_sorted_array_to_1d_array(arr):
    ans=[]
    
    min_heap=[]
    
    row=len(arr)
    col=len(arr[0])
    
    for i in range(col):
        heapq.heappush(min_heap,(arr[i][0],i,0))
        
    while min_heap:
        
        curr_data,curr_row,curr_col=heapq.heappop(min)
        ans.append(curr_data)
        
        if (curr_col+1<col):
            heapq.heappush(min_heap,(arr[curr_row][curr_col+1],curr_row,curr_col+1))
            
            
    return ans
    
    
