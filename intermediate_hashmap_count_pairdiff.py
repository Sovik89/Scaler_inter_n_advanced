# You are given an array A of N integers and an integer B. 
# Count the number of pairs (i,j) such that A[i] - A[j] = B and i ≠ j. 
# Since the answer can be very large, return the remainder after 
# dividing the count with 10**9+7.


def solve(A,B):
        count=0
        hashmap=dict()    
        for num in A:
            # We first populate the hashmap with frequency of numbers in A
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
            
        for i in A:
            # if i-B is present we add it to count since it will cover all i-B and i pairs
            if i-B in hashmap:
                count+=hashmap[i-B]
                    
        return count % ((10**9) + 7)