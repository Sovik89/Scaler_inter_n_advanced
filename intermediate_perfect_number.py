# You are given an integer A. You have to tell whether it is a perfect number or not.

# Perfect number is a positive integer which is equal to the sum of its proper positive divisors.

# A proper divisor of a natural number is the divisor that is strictly less than the number.


def solve(A):
    i=1
    count=0
    
    while i*i<=A:
       if A%i==0:
           if A//i==A:
               if A !=1:# For the prime numbers
                   count+=i
           else:
                count+=i
                count+=(A//i)
       
       i+=1
       
    if count == A:
        return 1
    else:
        return 0
    
    
print(solve(6))
        
    
                
    