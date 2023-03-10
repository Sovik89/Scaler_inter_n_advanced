def solve(A):
        if A==1:
            return 0
        i=2
        count=0
        while i*i<=A:
            if A%i==0:
                count+=1
            i+=1
        if count==0:
            return 1
        else:
            return 0
        

print(solve(8))