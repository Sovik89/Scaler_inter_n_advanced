def solve(A):
    Hashap_open={"(":1,"{":2,"[":3}
    Hashap_close={")":1,"}":2,"]":3}
    n=len(A)
    stacks=[]
    for item in range(n):
        if stacks:
            if A[item] in Hashap_open:
                stacks.append(A[item])
            elif A[item] in Hashap_close:
                if stacks[-1] in Hashap_close:
                    stacks.append(A[item])                
                elif Hashap_close[A[item]] == Hashap_open[stacks[-1]]:
                    stacks.pop()
                else:
                    stacks.append(A[item])
        else:
            stacks.append(A[item])
    
    if stacks:
        return 0
    else:
        return 1
    
    
print(solve("{([])}"))  
print(solve("(){"))  
print(solve("()[]"))
#print(solve("))))))))"))    