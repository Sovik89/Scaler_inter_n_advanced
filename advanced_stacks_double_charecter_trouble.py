def solve( A):
        stack=[]

        i=0
        n=len(A)
        while i<n:
            if stack:
                
                if stack[-1]!=A[i]:
                    stack.append(A[i])
                else:
                    stack.pop()
            else:
                stack.append(A[i])
            
            i+=1
        
        output=""

        while stack:
            output+=stack.pop()

        return output[::-1]
    
    
print(solve("abccbc"))