def solve(A):
        n=len(A)

        if n==1:
            return A[0]
        if A[0]!=A[1]:
            return A[0]

        if A[n-1]!=A[n-2]:
            return A[n-1]
        
        l,h=1,n-2

        while l<=h:
            m=(l+h)//2
            if A[m]!=A[m-1] and A[m]!=A[m+1]:
                return A[m]
            if A[m]==A[m-1]:#second c+occurance
                m-=1
            if m%2==0:
                l=m+2#element is on the right
            else:
                h=m-1#element is on the left