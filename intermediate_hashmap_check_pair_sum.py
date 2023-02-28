def solve(A, B):
        # Given an Array of integers B, and a target sum A.
        # Check if there exists a pair (i,j) such that Bi + Bj = A and i!=j.
        n=len(B)
        hashmap=dict()
        #hashmap for the frequency of the values present in the list
        for i in range(n):
            if B[i] not in hashmap:
                hashmap[B[i]]=1
            else:
                hashmap[B[i]]+=1
                
        #print(hashmap)
        flag=0
        #check if there exisits a value in hashmap with value A-B[i], if A-B[i]==B[i], check 
        #if there are more than 1 value values present
        
        for i in range(n):
            if (A-B[i]) in hashmap:
                if (A-B[i])==B[i]:
                    if hashmap[B[i]]>1:
                        flag=1
                        return flag
                else:
                    flag=1
                    return flag
        
        return flag