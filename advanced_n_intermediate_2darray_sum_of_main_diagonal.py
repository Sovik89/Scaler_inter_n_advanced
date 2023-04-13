def solve(self, A):
        ################first approach###########
        # row=len(A)
        # col=len(A[0])
        # i=0
        # j=0
        # sum_diagonal=0
        # while i<row and j<col:
        #     if i==j:
        #         sum_diagonal+=A[i][j]
        #     i+=1
        #     j+=1

        # return sum_diagonal
        
        ####################second approach#############################

        n=len(A)
        sum_diagonal=0
        for i in range(n):
            sum_diagonal+=A[i][i]

        return sum_diagonal