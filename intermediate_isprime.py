"""_summary_
    Given an Integer A. Return 1 if A is prime and return 0 if not.

"""

def solve(A):
        count = 0
        i=1
        while i*i<=A:
            if A%i == 0:
                if A//i == i:
                    count+=1
                else:
                    count+=2
            i+=1
           
        if count == 2:
            return 1
        else:
            return 0
        
        
print(solve(21))#O/P:0
print(solve(23))#O/P:1