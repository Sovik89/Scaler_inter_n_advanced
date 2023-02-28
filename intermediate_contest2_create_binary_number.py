def solve(A, B):
    value=""
    for i in range(A):
        value+="1"
    
    for j in range(B):
        value+="0"
    
    int_val=int(value)
    ans=0
    
    for i in range(len(value)):
        temp=int_val%10
        ans+=temp*(2<<i)
        int_val//=10
    
    return ans

print(solve(3,2))