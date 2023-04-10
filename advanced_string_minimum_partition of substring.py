def partitionString(s: str) -> int:
        
        j=0
        n=len(s)
        hash_set=set()
        
        count=0
        while j<n:
            if s[j] not in hash_set:
                hash_set.add(s[j])
                j+=1
                
            else:
                s=s[j:n]
                n=n-j
                j=0
                hash_set=set()
                count+=1       
                
                
        return count+1
    
    
print(partitionString("abacaba"))
#print(partitionString("ssssss"))