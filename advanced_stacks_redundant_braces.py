def braces(A):
    
    n=len(A)
    stacks=[]
    for i in range(n):
        if A[i]==")":
            if stacks and stacks[-1]=="(":
                return 1
            else:
                while stacks[-1]!="(" and stacks:
                    stacks.pop()
                stacks.pop()
        if A[i] in "+-/*(":
            stacks.append(A[i])
            
    return 0

print(braces("((a+b))"))   