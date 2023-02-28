def solve(self, A):
    i=0
    swaps=0
    N=len(A)
    
    while i < N:
        correct_index=A[i]
        if A[i]!=A[correct_index]:
            A[i],A[correct_index]=A[correct_index],A[i]
            swaps+=1
        else:
            i+=1
            
    return swaps