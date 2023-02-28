# You are given an array A of integers of size N.

# Your task is to find the equilibrium index of the given array

# The equilibrium index of an array is an index such that the sum of elements at lower indexes is 
# equal to the sum of elements at higher indexes.

# If there are no elements that are at lower indexes or at higher indexes, then the corresponding 
# sum of elements is considered as 0.

# Note:

# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.

import sys

def solve(A):
    #create the prefix sum of the given array
    pf_sum= []
    n=len(A)
    min_equi_index=-sys.maxsize
    
    