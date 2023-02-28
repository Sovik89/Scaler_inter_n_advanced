from math import sqrt
from functools import cmp_to_key

def solve(A,B):
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    
    # Initially tried with Selection Sort till B iterations. Gives TLE error for Hard test case.


    # Using python inbuilt sort function, sorting the array taking the distance from origin as key.
    # return first B elements of the sorted array.
    
    #Better approach may be with heap sort
    
    def my_compare(a,b):
        x1,y1=a[0],a[1]
        x2,y2=b[0],b[1]
        
        eucl_x1=sqrt(x1**2+y1**2)
        eucl_x2=sqrt(x2**2+y2**2)
        
        if eucl_x1<eucl_x2:
            return -1
        else:
            return 1
        
    
    A.sort(key=cmp_to_key(my_compare))
    
    return A[:B]

    

print(solve(
    [ 
       [1, 3],
       [-2, 2] 
     ],1
    
))
    