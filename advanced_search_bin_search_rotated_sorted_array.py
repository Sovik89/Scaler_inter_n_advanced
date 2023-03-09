def search(A, B):
        n=len(A)
        l=0
        h=n-1
        while l<=h:
            m=(l+h)//2

            if A[m]==B:
                return m
            #if left half sorted
            if A[m]>=A[l]:
                if B>=A[l] and B<A[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                #check if right half sorted
                if B>=A[m] and B<A[h]:
                    l=m+1
                else:
                    h=m-1

        return -1