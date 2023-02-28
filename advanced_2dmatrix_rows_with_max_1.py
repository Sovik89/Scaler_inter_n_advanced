import sys

def solve(A):
    row=len(A)
    col=len(A[0])
    max_count=-sys.maxsize
    max_row= 0
    for i in range(row):
        count=0
        for j in range(col):
            if A[i][j]==1:
                count+=1
        
        if max_count<count:
            max_row=i
            max_count=count
        
    return max_row
    
            
            
            
            
