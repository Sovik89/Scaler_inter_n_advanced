def solve(A, B):
    
    def kth_symbol(A):    
        
        if A==1:# if A is in 1st row value is 0 or base condition
            return "0"
        x=kth_symbol(A-1)# recursive function calling
        y=""

        for i in x:
            if i =="0":
                y+="01"
            elif i =="1":
                y+="10"
        print(y)
        return y# value to b returned after every calling
        
    return kth_symbol(A)[B]   
    
    
print(solve(4,4))