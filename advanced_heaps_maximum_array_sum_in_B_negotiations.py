import heapq

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    

    def solve(self, A, B):
        heapq.heapify(A)

        while B>0:
            val=heapq.heappop(A)
            heapq.heappush(A,-val)
            B-=1

        return sum(A)