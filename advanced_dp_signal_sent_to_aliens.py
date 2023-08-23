import sys
sys.setrecursionlimit(10**6)


######################DP with fibonacci#####################
class Solution:
    # @param A : integer
    # @return an integer
    def signals(self,n,dp):
        if n<=1:
            return n

        if dp[n]==-1:
            dp[n]=self.signals(n-1,dp)+self.signals(n-2,dp)

        return dp[n]%(1000000007)        


    def solve(self, A):

        mod=(10**9)+7
        
        dp=[-1]*(A+3)

        ans=self.signals(A+2,dp)

        return ans%mod

