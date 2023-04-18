class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n=len(A)
        output_list=list()
        
        for i in range(n):
            k=0
            j=i
            count=0
            temp_list=list()
            while k<n and j>=0:
                #print(A[k][j],end="")
                #if i!=(n-1):
                temp_list.append(A[k][j])
                j-=1
                k+=1
                count+=1
                
            while count<n:
                temp_list.append(0)
                count+=1
            output_list.append(temp_list)
                
            #print()
        
        for i in range(1,n):
            k=i
            j=n-1
            count=0
            temp_list=list()
            while k<n and j>=0:
                #print(A[k][j],end="")
                temp_list.append(A[k][j])
                k+=1
                j-=1
                count+=1
            #print()        
            
            while count<n:
                temp_list.append(0)
                count+=1
            output_list.append(temp_list)
        
        return output_list
