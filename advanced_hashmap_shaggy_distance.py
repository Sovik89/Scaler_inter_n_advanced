import sys

def solve(A):
    
    hash_map={}
    min_val=sys.maxsize
    
    for i in range(len(A)):
        length=0
        if A[i] not in hash_map:
            hash_map[A[i]]=i
        else:
            length=i-hash_map[A[i]]
            hash_map[A[i]]=i
            min_val=min(min_val,length)
            
    if min_val ==sys.maxsize:
        return -1
    else:
        return min_val
    
#print(solve([7, 1, 3, 4, 1, 7]))
print(solve([1, 1]))
