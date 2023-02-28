# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

def solve(A, B):
        sum_list = list()
        for positions in B:
            start,end = positions
            sum_val=0
            pos1=start-1
            pos2=end-1
            for i in range(pos1,pos2+1):
                sum_val+=A[i]
            sum_list.append(sum_val)
        return sum_list
    
print(solve([1, 2, 3, 4, 5],[[1, 4], [2, 3]]))#O/P:[10, 5]