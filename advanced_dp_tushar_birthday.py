class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
    def solve(self, A, B, C):
        max_appetite=max(A)
        N=len(B)#no of dishes

        # initialize cost array with infinity for all indices except cost[0], which is 0
        dp = [float('-inf')]*(max_appetite+1)
        dp[0]=0

        # for each dish, update the cost array with the minimum cost required to fill each eating capacity greater than or equal to B[i]
        for i in range(N):
            for cap in range (B[i],max_appetite+1):
                dp[cap]=min(dp[cap],dp[cap-B[i]]+C[i])

        total=0
        # compute the total cost required to fill each friend's eating capacity
        for appetite in A:
            total+=dp[appetite]

        return total