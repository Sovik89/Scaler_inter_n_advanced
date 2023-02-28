#Given an array A of N integers. Also given are two integers B and C. Reverse the array A in the given range [B, C]


def solve(A,B,C):
    
    pos1=B
    
    pos2=C
    
    while pos1<pos2:
        A[pos1],A[pos2]=A[pos2],A[pos1]
        
        pos1+=1
        pos2-=1
        
        
    return A


#print(solve([1, 2, 3, 4],2,3))#P/O: [1, 2, 4, 3]

    