def solve(A):
    
    n = len(A)
    temp=""
    sum=0
    for i in range(n):
        if A[i].isnumeric():
            temp+=A[i]
            if i<(n-1):
                if A[i+1].isnumeric()==False:
                    sum+=int(temp)
                    temp=""
                if A[i+1] == None and temp !="":
                    sum+=int(temp)
                    temp=""
    if temp!="":
        sum+=int(temp)
    
    return sum

print(solve("a12b34c"))
#print(solve("123"))
        