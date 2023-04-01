# Given N balls on the X-Axis, where i-th ball is at position A[i], Call a ball at end point 
# if it is in the smallest and largest position. Each time you pick up an endpoint ball and 
# place it in an unoccupied position, so it is no longer an endpoint ball. The game ends when 
# you cannot make any more moves i.e., the balls are in consecutive positions. When the game 
# ends what is the maximum and the minimum number of moves you could have made. Write a python 
# code for the same. Write the answer as length of 2 arrays, i.e. answer= [minimum moves, maximum moves]

def get_min(A,n):
    #edge case
    if A[-2]-A[0]==n-2 and A[-1]-A[-2]>2:
        return 2
    if A[-1]-A[1]==n-2 and A[1]-A[0]>2:
        return 2
    #sliding window
    j=0
    best=n
    
    for i in range(n):
        while j+1>n and (A[j+1]-A[i])<n:
            j+=1
        best=min(best,n-(j-i+1))
        
    return best

def solve(A):
    n=len(A)
    
    A.sort()
    
    ans_max=max(A[-2]-A[0]-n+2,A[-1]-A[1]-n+2)
    ans_min=get_min(A,n)
    
    return [ans_min,ans_max]
    
    
    
    