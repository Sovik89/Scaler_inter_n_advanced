# You are given an array of N integers, A1, A2 ,..., AN and an integer B. 
# Return the of count of distinct numbers in all windows of size B.

# Formally, return an array of size N-B+1 where i'th element in this array 
# contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

# NOTE: if B > N, return an empty array.

def dNums(A, B):
        
        window_array=[]
        n=len(A)
        distinct_hashmap=dict()
        #create the haspmap for distinct values the first B numbers
        for i in range(B):
            if A[i] not in distinct_hashmap:
                distinct_hashmap[A[i]]=1
            else:
                distinct_hashmap[A[i]]+=1
        window_array.append(len(distinct_hashmap))
        
        start=1
        end=B
        
        # using slidong window technique of length B till end reaches len(A) we find distinct value, 
        # if value=0, delete the key
        # else if not present introduce the key value pair, else add the freq

        while end<n:
            #remove the first element in the window
            distinct_hashmap[A[start-1]]-=1
            if distinct_hashmap[A[start-1]]==0:
                del distinct_hashmap[A[start-1]]
            #add the next element outside the window
            if A[end] not in distinct_hashmap:
                distinct_hashmap[A[end]]=1
            else:
                distinct_hashmap[A[end]]+=1
            window_array.append(len(distinct_hashmap))

            start+=1
            end+=1
        
        return window_array