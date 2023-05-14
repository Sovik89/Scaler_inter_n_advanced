def solve(A, B, C):

        max_min_val=float('-inf')

        for i in range(1,A):

            # we check minimum candies distributed for all combination of peoples
            val=min(B//i,C//(A-i))
            #we find the maximum amongst the minimum that could be distributed
            max_min_val=max(max_min_val,val)

        return max_min_val