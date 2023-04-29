import heapq,math

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def eucledian_distance(self,x,y):
        square_val=(x**2)+(y**2)
        return math.sqrt(square_val)
        
    def solve(self, A, B):
        min_heap=[]
        #hash_map=dict()
        
        n=len(A)
        
        for i in range(n):
            xi=A[i][0]
            yi=A[i][1]
            
            euc_dist=self.eucledian_distance(xi,yi)
            
            #hash_map[euc_dist]=A[i]
            
            heapq.heappush(min_heap,(euc_dist,A[i]))
            
        output_list=[]
        
        for j in range(B):
            val,point=heapq.heappop(min_heap)
            output_list.append(point)
            
        return output_list

print(solve([ 
       [1, -1],
       [2, -1]
     
     ],1))  