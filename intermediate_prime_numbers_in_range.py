"""
   You will be given an integer n. You need to return the count of prime numbers less than or equal to n. 
    
"""

def solve(A):
    count_prime=0
    for j in range(1,A+1):
        count = 0
        i=1
        while i*i<=j:
            if j%i == 0:
                if j//i == i:
                    count+=1
                else:
                    count+=2
            i+=1
            
        if count == 2:
            #print(j,=",end ")
            count_prime+=1
    
    return count_prime

print(solve(20))#O/P:8
            
    