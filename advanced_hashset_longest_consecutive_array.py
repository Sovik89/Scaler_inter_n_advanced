def longestConsecutive( A):
    n=len(A)
    hash_set=set()
    hash_set=set(A)
    ans=1
    
    for x in hash_set:
        
        if x-1 not in hash_set:
            l=0
            y=x
            while y in hash_set:
                l+=1
                y+=1
                
            ans=max(ans,l)
            
    return ans


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
    