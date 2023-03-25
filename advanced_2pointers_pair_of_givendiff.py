def solve(A, B):
    A.sort()
    n=len(A)-1
    
    p1=0
    p2=1
    
    count=0
    target=abs(B)
    hash_set=set()
    while p2<n:
        
        if A[p2]-A[p1]>target:
            p1+=1
        elif A[p2]-A[p1]<target:
            if p2<=n-1:           
                p2+=1
            else:
                break            
        else:
            
            if tuple([A[p1],A[p2]]) not in hash_set:
                hash_set.add(tuple([A[p1],A[p2]]))
            if p2<=n-1 and p1<=n-2:
                p1+=1
                p2+=1
            else:
                break
    while p1<p2+1:
        if A[p2]-A[p1]==target:
            if tuple([A[p1],A[p2]]) not in hash_set:
                hash_set.add(tuple([A[p1],A[p2]]))
        p1+=1
    return len(hash_set)

#print(solve([1, 5, 3, 4, 2],3))
print(solve([8, 12, 16, 4, 0, 20],4))
#print(solve([1, 1, 1, 2, 2],0))