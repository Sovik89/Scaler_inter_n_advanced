def sqrt(A):
        if A==0:
            return 0
        h=A
        l=1

        while l<=h:
            m=(l+h)//2

            
            if m**2<=A<(m+1)**2:
                return m
            if A<m**2:
                h=m-1
            else:
                l=m+1