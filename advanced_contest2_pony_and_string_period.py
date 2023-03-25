def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def solve(A):
    #Idea lets take the frequency of all the letters in A in a hash_map
    
    hash_map={}
    
    n=len(A)
    
    for i in range(n):
        if A[i] not in hash_map:
            hash_map[A[i]]=1
        else:
            hash_map[A[i]]+=1
    
    general_gcd=None
            
    #We now go for the GCD in Associative Law
    n1=len(hash_map)
    for i in hash_map:
        #print(i)
        if general_gcd == None:
           general_gcd=hash_map[i]
        else: 
            general_gcd=gcd(general_gcd,hash_map[i])
        
    
    #now we take the sum of freq[i]/general_gcd and return
    
    sum_period=0
    
    for i in hash_map:
        sum_period+=(hash_map[i]//general_gcd)
        
    return sum_period


print(solve("abacbc"))
        
        
    