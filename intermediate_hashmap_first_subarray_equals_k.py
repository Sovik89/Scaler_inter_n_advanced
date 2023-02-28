# Given an array of positive integers A and an integer B, 
# find and return first continuous subarray which adds to B.

# If the answer does not exist return an array with a single element "-1".

# First sub-array means the sub-array for which starting index in minimum.


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
                #count += 1
                return A[:i+1]
            #if pf[i]-B is present in the dict we add the frequency to the count
            if pf[i]-B in dict1:
                if pf.index(pf[i]-B) > i:
                    return A[i+1:pf.index(pf[i]-B)+1]
                else:
                    return A[pf.index(pf[i]-B)+1:i+1]
                #count+=dict1[pf[i]-B]
            # if pf[i] present in the dict we add the freq else we introduce it in the dict
            if pf[i] in dict1:
                dict1[pf[i]] += 1
            else:
                dict1[pf[i]] = 1
    
        return [-1]


#print(solve([1, 2, 3, 4, 5],5))
print(solve([5, 10, 20, 100, 105],110))