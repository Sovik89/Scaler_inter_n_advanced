def colorful(A):       
        
        digitList=[]# Splitiing the number into individual digits of the same number
        
        while A:
            temp=A%10
            digitList.append(temp)
            A//=10
        
        #keeping the values as the seqience of the number was
        digitList=list(reversed(digitList))
        
        n=len(digitList)
        
        hash_set=set()
        
        for i in range(n):
            prod=1
            for j in range(i,n):
                prod*=digitList[j]
                #check if the prod is in the hash set
                if prod in hash_set:
                    return 0
                else:
                    hash_set.add(prod)
        return 1