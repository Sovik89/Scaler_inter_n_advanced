class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n=len(A)
        i=0
        j=n-1
        diff=0
        while i<j:

            if A[i] != A[j]:
                diff+=1
            if diff>1:
                return "NO"

            i+=1
            j-=1
        if i==j and (diff==0) or (diff==1):
            return "YES"
        if i>j and (diff==1):
            return "YES"
        else:
            return "NO"

        
        
