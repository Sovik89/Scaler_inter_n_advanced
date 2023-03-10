def solve(A):
    #Input is the upper range from 1 to N
    #O/P: list of integers which are primr
    
    doors=[0]*(A+2)#0 represents prime and 1 represents divisible. We assume all of the values are prime at first
    
    #0th and First element is negated by default
    ans=[]
    for value in range(2,A+1):
        if doors[value]==0:
            for i in range(value*2,A+1,value):
                if doors[i]!=1:
                    doors[i]=1
        
    
    for i in range(2,A+1):
        if doors[i]==0:
            ans.append(i)
            
    return ans


print(solve(7))
              
    
    
    
    
    
    

    