# Given an array of integers A and an integer B.
# Find the total number of subarrays having sum equals to B.
# Input Format:
# The first argument given is the integer array A.The second argument given is integer B.
# Output Format:
# Return the total number of subarrays having sum equals to B.

def solve( A, B):
        n = len(A)
        pf = []
        summ = 0
        # creating the prefix sum array 
        for i in range(n):
            summ += A[i]
            pf.append(summ)
        
        dict1 = {}
        count = 0
        for i in range(n):
            #if the value in the prefix array is equal to B we add it in the count
            if pf[i] == B:
                count += 1
            #if pf[i]-B is present in the dict we add the frequency to the count
            if pf[i]-B in dict1:
                count+=dict1[pf[i]-B]
            # if pf[i] present in the dict we add the freq else we introduce it in the dict
            if pf[i] in dict1:
                dict1[pf[i]] += 1
            else:
                dict1[pf[i]] = 1
    
        return count
    


print(solve([1, 0, 1],1))