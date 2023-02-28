# You are given an array A of N integers and an integer B. 
# Count the number of pairs (i,j) such that A[i] + A[j] = B and i ≠ j. 
# Since the answer can be very large, return the remainder after dividing the count with 10**9+7.

# Note - The pair (i,j) is same as the pair (j,i) and we need to count it only once.

def solve(A, B):        
    c = 0
    hash_ = dict()
    d = (10**9) + 7
    for i in range(len(A)):
        # The idea here is to find the difference with the number, i.e. A[i]+A[j]=B, 
        # the diff being b=B-A[j], 
        # if b is not present in the hashmap, 
        # we check if A[i] is present
        # or not, if A[i] is not present introduce A[i] in the hashmap, 
        # i.e. hashmap{A[i]}=1, if A[i] is present
        # in the hashmap, then add the frequency,hashmap{A[i]}+=1,if 
        # if b is present in the hashmap,
        # add the count with the freq of hashmap[A[b]], this way if there is more than 1 b
        # we can tally it in the count
        # Eg. B=4,  we have one 1 and two 3's, we will get the count as 2
        b = B - A[i]
        if b in hash_:
            c+=hash_[b]
        if A[i] in hash_:
            hash_[A[i]]+=1
        else:
            hash_[A[i]]=1      
    return c%d


print(solve([3, 5, 1, 2],8)) 