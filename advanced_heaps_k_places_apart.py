import heapq as heapq

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    

    def solve(self, A, B):
        ans=[]
        
        min_heap=[]

        #for first B+1 integers
        for i in range(B+1):
            heapq.heappush(min_heap,A[i])

        #for B+1 to n
        for j in range(B+1,len(A)):
            ans.append(heapq.heappop(min_heap))
            heapq.heappush(min_heap,A[j])

        #append residual values in min_heap

        while min_heap:
            ans.append(heapq.heappop(min_heap))


        return ans


        
        

