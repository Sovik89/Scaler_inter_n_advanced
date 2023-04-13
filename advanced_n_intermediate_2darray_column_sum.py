class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        row=len(A)
        col=len(A[0])
        sum_list=list()
        for j in range(col):
            sum_val=0
            for i in range(row):
                sum_val+=A[i][j]
            #print(sum_val)
            sum_list.append(sum_val)
        return sum_list
