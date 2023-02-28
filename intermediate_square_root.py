"""
    Given a number A. Return square root of the number if it is perfect square otherwise return -1.   
    
"""


def solve(A):
    
    i=1
    
    while i*i<=A:
        if i*i==A:
            return 1
        i+=1
        
    return -1


print(solve(24))#o/P: -1

print(solve(25))#O/P: 1