#import sys

def solve(A):
    
    
    set_A=set()
    
    for values in A:
        first,second=values
        if (first,second) not in set_A:
            set_A.add((first,second))

    return len(set_A)





print(solve([[5, 6],[2, 8],[-1, -1],[2, -3],[2, 8],[7, 7],[2, -3]]))