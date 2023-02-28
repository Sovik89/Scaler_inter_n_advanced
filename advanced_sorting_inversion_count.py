class Solution:
    # @param A : list of integers
    # @return an integer
    # count=0
    def solve(self, A):
        
        n=len(A)
        result=self.mergesort(A,0,n-1)

        return (result)%1000000007

    def mergesort(self,arr,start,end):
        if start == end:
            return 0
        mid = (start+end)//2

        X=self.mergesort(arr,start,mid)
        Y=self.mergesort(arr,mid+1,end)
        Z=self.merge_subarrays(arr,start,mid,end)
        inversion_count=X+Y+Z

        return inversion_count

    def merge_subarrays(self,arr,start,midElement,end):
        count=0
        p1= start
        p2=midElement+1
        p3=0

        tempArray=[0]*(end-start+1)

        while (p1 <= midElement and p2 <= end):
            if arr[p1] <= arr[p2]:
                tempArray[p3] = arr[p1]
                p1 += 1
                p3 += 1
                
            else:
                count+=midElement-p1+1
                tempArray[p3] = arr[p2]
                p2 += 1                
                p3 += 1
        
        #Copying remaining elements
        while p1 <= midElement:
            tempArray[p3] = arr[p1]
            p1 += 1
            p3 += 1
        
        #Copying remaining elements
        while p2 <= end:
            tempArray[p3] = arr[p2]
            p2 += 1
            p3 += 1
        
        # copying the sorted tempArray (merged two sub arrays) to main array
        i = start
        j = 0 

        while i <= end:
            arr[i] = tempArray[j]
            i += 1
            j += 1
        
        return count
