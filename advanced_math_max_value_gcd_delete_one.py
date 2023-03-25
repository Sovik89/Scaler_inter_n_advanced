def gcd(a,b):
    if b==0:
        return a
    
    return gcd(b,a%b)

def solve(A):
    # Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) 
    # of the remaining array is maximum.

    # Find the maximum value of GCD.
    
    n=len(A)
    
    pf_array=[0]*n
    suffix_array=[0]*n
    
    pf_array[0]=A[0]
    suffix_array[n-1]=A[n-1]
    
    for i in range(n):
        pf_array[i]=gcd(pf_array[i-1],A[i])
    
    for i in range(n-2,-1,-1):
        suffix_array[i]=gcd(suffix_array[i+1],A[i])
        
    # print(pf_array)
    # print(suffix_array)
    
    max_val=-1
    
    for i in range(n):
        if i==0:
            max_val=max(max_val,suffix_array[i+1])
        elif i==n-1:
            max_val=max(max_val,pf_array[i-1])
        else:
            max_val=max(gcd(pf_array[i-1],suffix_array[i+1]),max_val)
    
    return max_val


#print(solve([5,15,30]))
print(solve([12,15,18]))
    