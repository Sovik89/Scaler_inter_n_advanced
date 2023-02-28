# Given a matrix of integers A of size N x M and multiple queries Q, for each query, 
# find and return the submatrix sum.

# Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

# NOTE:

# Rows are numbered from top to bottom, and columns are numbered from left to right.
# Sum may be large, so return the answer mod 109 + 7.


# @param A : list of list of integers
# @param B : list of integers
# @param C : list of integers
# @param D : list of integers
# @param E : list of integers
# @return a list of integers
def solve( A, B, C, D, E):
    #my approach to think
    
    # row=len(A)
    # col=len(A[0])
    
    # #we create a new array for the prefix sum matrix
    
    # newA=[[0 for i in range(row)] for j in range(col)]
    
    # #row wise prefix sum
    # for j in range(row):
    #     sums = 0
    #     for i in range(col):
    #          sums+=A[i][j]
    #          newA[i][j]=sums
             
    # #column wise prefix sum on the new matrix values
    
    # for i in range(col):
    #     sums = 0
    #     for j in range(row):
    #         sums+=A[i][j]
    #         newA[i][j]=sums
    
    # ans=[]
    
    # for i in range(B):
    #    x1=B[i]-1
    #    x2=C[i]-1
    #    y1=D[i]-1
    #    y2=E[i]-1
       
    #    s = newA[x2][y2]
       
    #    if x1 != 0 and y1 != 0 :
    #         ans.append((s - newA[x1-1][y2] - newA[x2][y1-1] + newA[x1-1][y1-1]) % (10**9 + 7))
    #    elif x1 == 0 and y1 != 0 :
    #         ans.append((s - newA[x2][y1-1]) % (10**9 + 7))
    #    elif x1 != 0 and y1 == 0 :
    #         ans.append((s - newA[x1-1][y2]) % (10**9 + 7))
    #    else :
    #         ans.append(s % (10**9 + 7))
            
    # return ans
    
    
    #####running approach#####
    
        n = len(A)
        m = len(A[0])
        for j in range(m) :
            sums = 0
            for i in range(n) :
                sums += A[i][j]
                A[i][j] = sums
        for i in range(n) :
            sums = 0
            for j in range(m) :
                sums += A[i][j]
                A[i][j] = sums
        ans = []
        for i in range(len(B)) :
            a1 = B[i] - 1
            b1 = C[i] - 1
            a2 = D[i] - 1
            b2 = E[i] - 1
            if a1 != 0 and b1 != 0 :
                ans.append((A[a2][b2] - A[a1-1][b2] - A[a2][b1-1] + A[a1-1][b1-1]) % (10**9 + 7))
            elif a1 == 0 and b1 != 0 :
                ans.append((A[a2][b2] - A[a2][b1-1]) % (10**9 + 7))
            elif a1 != 0 and b1 == 0 :
                ans.append((A[a2][b2] - A[a1-1][b2]) % (10**9 + 7))
            else :
                ans.append((A[a2][b2]) % (10**9 + 7))
        return ans
           