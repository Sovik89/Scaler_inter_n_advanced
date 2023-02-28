def solve(A,B):
    """
    Solution approach:

        we take a prefix sum of all the sum till length.Init sum=0
        we take count of array sum divisible by B,count=0
        and we take a hashmap of remainder.Init rem[0]=1

        We add value into sum and we take the remainder
        if remainder is not present we hashmap we add count = previous 
        value of rem[sum%B] and add the frequency of rem[sum%B]

        for negetive sum:
            
            if remainder is negetive

            Bn-y<0
            then,
            Bn-y+B-B
            B(n-1)+B-y
            B*n'+B-y
    """
    
    sum_val=0
    remainder_map={}
    remainder_map[0]=1
    count=0
    rem=0
    n = len(A)
    
    for i in range(n):
        sum_val+=A[i]
        rem=sum_val%B
        
        if rem<0:
            rem+=B
            
        if rem in remainder_map:
            count+=remainder_map[rem]
            remainder_map[rem]+=1
        else:
            remainder_map[rem]=1
    
    return count
    

print(solve([2,3,5,4,5,3,4],7))
        
            