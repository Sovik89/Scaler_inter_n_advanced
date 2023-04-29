import heapq

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n=len(A)
        max_heap=[]#box1/left
        min_heap=[]#box2/right
        heapq.heappush(max_heap,-A[0])
        ans=[A[0]]
        for i in range(1,n):
            #insert to max_heap or min_heap
            if A[i]<-max_heap[0]:
                heapq.heappush(max_heap,-A[i])
            else:
                heapq.heappush(min_heap,A[i])
            # check if transerring is required
            if len(max_heap)<len(min_heap):
                val=heapq.heappop(min_heap)
                heapq.heappush(max_heap,-val)
            elif (len(max_heap)-len(min_heap))>1:
                val=heapq.heappop(max_heap)
                heapq.heappush(min_heap,-val)
            #check the lenght of the array traversed so far, odd length or even
            s=i+1

            # for normal running median

            # if s%2==0:
            #     val=(-max_heap[0]+min_heap[0])//2
            #     ans.append(val)
            # else:
            #     ans.append(-max_heap[0])

            #for the specific answer required in the problem problem
            # NOTE:

            #     If the number of elements is N in B and N is odd, then consider the median as B[N/2]
            #      ( B must be in sorted order).
            #     If the number of elements is N in B and N is even, then consider the median as B[N/2-1].
            #      ( B must be in sorted order).
            
            ans.append(-max_heap[0])
        return ans