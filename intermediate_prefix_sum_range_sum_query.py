# Description

# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.


def rangeSum(A,B):
    
    # A is the list of integers on which the activity needs to be performed
    # B is the MX2 matrix which contains the lower an the higher value on which the sum needs to be performewd
    
    prefix_array=[]
    output_list=[]
    sum_val=0
    n = len(A)
    
    #creating the prefix array
    for i in range(n):
        sum_val+=A[i]
        prefix_array.append(sum_val)
        
    #print(prefix_array)
    
    # checking the range array to find out the lower and the upper range
    
    for lower,upper in B:
        
            if lower ==0:
                output_list.append(prefix_array[upper])
                
            else:
                diff= prefix_array[upper]-prefix_array[lower-1]
                output_list.append(diff)
    
    return output_list


print(rangeSum([1, 2, 3, 4, 5],[[0, 3], [1, 2]]))
#print(rangeSum([2, 2, 2],[[0, 0], [1, 2]]))



        
            
            
         
        