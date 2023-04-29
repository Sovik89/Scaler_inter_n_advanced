import heapq

class Solution:
    # @param A : list of integers
    # @return an integer
    def median_finder(self,arr):
        n=len(arr)
        max_heap=[]#box1/left
        min_heap=[]#box2/right
        heapq.heappush(max_heap,-arr[0])
        #ans=[arr[0]]
        if n==1:
            return False

        #most important validation
        if arr[0]==arr[1]:
            return True
        for i in range(1,n-1):
            #insert to max_heap or min_heap
            if arr[i]<-max_heap[0]:
                heapq.heappush(max_heap,-arr[i])
            else:
                heapq.heappush(min_heap,arr[i])
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

            if s%2==0:
                val=(-max_heap[0]+min_heap[0])/2
                #ans.append(val)
                
            else:
                val=-max_heap[0]
                
            if val == arr[i+1]:
                return True            

        return False

    def solve(self, A):
        B=A[::-1]
    
        forward_val=self.median_finder(A)
        
        reverse_val=self.median_finder(B)
        
        if forward_val or reverse_val:
            return 1       
        
        return 0