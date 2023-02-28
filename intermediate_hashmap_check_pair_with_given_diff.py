# Given an one-dimensional unsorted array A containing N integers.

# You are also given an integer B, find if there exists a pair of elements 
# in the array whose difference is B.

# Return 1 if any such pair exists else return 0.

def solve(A, B):
        count=0
        hashmap=dict()  
        #create hashmap with frequency of each value  
        for num in A:
            
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        # if difference is B>0, we chech if B>=i, then we check i+B in hashmap, else we check i-B
        # if difference is B=0, we check  hashmap[i]>1 we return 1    
        for i in A:
            if B!=0:
                if B>=i:
                    if i+B in hashmap:
                        return 1
                else:
                    if i-B in hashmap:
                        return 1
            else:
                if hashmap[i]>1:
                    return 1
                    
        return 0
    
    
print(solve([5, 10, 3, 2, 50, 10],0))