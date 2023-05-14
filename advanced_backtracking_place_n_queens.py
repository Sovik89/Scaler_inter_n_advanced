#untested

def validQ(mat,i,j):
    #for column checks
    n=i
    for k in range(n):
        if mat[k][j]==1:
            return 0
        

    #for left diagonal:
    k=i
    l=j
    
    while k>=0 or l>=0:
        if mat[k][l]==1:
            return 0
        k-=1
        l-=1
        
        
    #for right diagonal
    
    k=i
    l=j
    m=len(mat[0])
    
    while k>=0 or l<=m:
        if mat[k][l]==1:
            return 0
        k-=1
        l+=1
        
    return 1



def placeNQueens(mat,i,N):
    if i == N:
        print(mat)
        return
    
    for j in range(N):
        if validQ(mat,i,j):
            mat[i][j]=1
            placeNQueens(mat,i+1,N)
            mat[i][j]=0
        
    
    
    