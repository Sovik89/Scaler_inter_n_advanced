def solve(A):    
    """
    Summary:
    
    Given an array A of N integers.

    Find the length of the longest subarray in the array which sums to zero.
    
    """
    
    n=len(A)
    pf_array=[]
    sum_val=0
    longest_sa_of_0=0
    # creating prefix array
    for i in range(n):
        sum_val+=A[i]
        pf_array.append(sum_val)
        
    hash_map_freq=dict()
    # keeping the location of prefix values in dict and comparing any duplicate's
    # longest length and also 0th val should be dealth seperately
    for i in range(n):
        if pf_array[i] not in hash_map_freq:
            if pf_array[i]==0:
                longest_sa_of_0=max(longest_sa_of_0,i+1)
                
            hash_map_freq[pf_array[i]]=[i]
        else:
            temp=[i]
            hash_map_freq[pf_array[i]].extend(temp)
            longest_sa_of_0=max(longest_sa_of_0,
                                (i-hash_map_freq[pf_array[i]][0])  
                                )

    return longest_sa_of_0




print(solve([1, -2, 1, 2]))#O/P:3



    
     