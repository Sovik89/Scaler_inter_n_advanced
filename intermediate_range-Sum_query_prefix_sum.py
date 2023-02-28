# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

def rangeSum(self, A, B):
    prefix_sum_list = list()
    output_list = list()
    sum_val = A[0]
    prefix_sum_list.append(sum_val)
    for i in range(1,len(A)):
        sum_val+=A[i]
        prefix_sum_list.append(sum_val)
    
    for ranges in B:
        pos1,pos2 = ranges
        if pos1 == 1:
            diff = prefix_sum_list[pos2-1]
            output_list.append(diff)
        else:
            diff = prefix_sum_list[pos2-1]-prefix_sum_list[pos1-2]
            output_list.append(diff)
                        
        
        return output_list