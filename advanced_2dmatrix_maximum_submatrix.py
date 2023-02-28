import sys

def solve( A):
        def prefixSum(a1,b1,a2,b2,arr):
            sums = 0
            
            if a1 != 0 and b1 != 0 :
                sums=arr[a2][b2] - arr[a1-1][b2] - arr[a2][b1-1] + arr[a1-1][b1-1]
            elif a1 == 0 and b1 != 0 :
                sums=arr[a2][b2] - arr[a2][b1-1]
            elif a1 != 0 and b1 == 0 :
                sums=arr[a2][b2] - arr[a1-1][b2]
            else :
                sums=arr[a2][b2]
            return sums
        
        n = len(A)
        m = len(A[0])
        #we create a new array where prefix sums are to be created
        newA=[[0 for i in range(m)] for j in range(n)]
        #print(newA)
        
        # prefix sum rowwise
        for j in range(m) :
            sums = 0
            for i in range(n) :
                sums += A[i][j]
                newA[i][j] = sums
                
        # prefix sum column wise
        for i in range(n) :
            sums = 0
            for j in range(m) :
                sums += newA[i][j]
                newA[i][j] = sums
        
        max_val=-sys.maxsize
        
        #print(newA)
        
        # calculate the prefix sum of each submatrix and find maximum of it

        for i in range(n):
            for j in range(m):
                sum_val=prefixSum(i,j,n-1,m-1,newA)
                max_val=max(max_val,sum_val)
                

        return max_val
    
    
        
            
    
print(solve([[-42],[-41],[-37],[-29],[-23]]))

# print(solve([[-8, 1, 1],
# [-1, 6, 6],
# [7, 10, 10]]))