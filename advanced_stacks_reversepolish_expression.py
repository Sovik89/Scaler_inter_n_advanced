def evalRPN(A):
    n=len(A)
    stacks=[]
    
    for i in range(n):
        if A[i] in "+/*-":
            second_val=int(stacks.pop())
            first_val=int(stacks.pop())
            
            expression=0
            if A[i]=="+":
                expression=first_val+second_val
            elif A[i]=="-":
                expression=first_val-second_val
            elif A[i]=="*":
                expression=first_val*second_val
            else:                
                expression=first_val//second_val            
            stacks.append(str(expression))
        else:
            stacks.append(A[i])
            
    final_val=stacks.pop()
    
    return final_val

print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
     