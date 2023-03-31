def solve(A, B, C):
    
    
    stack=[]
    #stack.append(B)
        
        
    for i in range(A):
            if stack:
                if C[i]==0:
                    stack.pop()
                else:
                    stack.append(C[i])
            else:
                if C[i]!=0:
                    stack.append(C[i])       
        
    if stack:
            return stack[-1]
    else:
            return B
    
    

print(solve(10,23,[86, 63, 60, 0, 47, 0, 99, 9, 0, 0]))
print(solve(1,1,[2]))
print(solve(1,1,[0]))
        
        