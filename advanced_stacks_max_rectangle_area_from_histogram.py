"""

        Approach:
        1.For each bar in the histogram, we want to find the largest rectangle that can be formed using 
        that bar.
        To do this, we need to find the left and right boundaries of the rectangle.

        2.We can use a stack to keep track of the indices of bars that have not been processed yet.
         We start with an empty stack.

        3.We iterate over the bars in the histogram from left to right.
        For each bar, we pop elements off the stack until we find a bar whose height is less than 
        the current bar.
        The left boundary of the rectangle formed by the current bar is the index of the previous 
        bar in the stack.
        If the stack is empty, then the left boundary is 0.

        4.We push the index of the current bar onto the stack.
        5.We repeat steps 3-4 for each bar in the histogram.

        6.Once we have calculated the left boundaries of all the bars,
        we clear the stack and repeat steps 3-4,
        but this time iterating over the bars in the histogram from right to left.
        The right boundary of the rectangle formed by the current bar is the index of the next bar 
        in the stack.
        If the stack is empty, then the right boundary is N-1, where N is the length of the histogram.

        7.Once we have calculated the left and right boundaries of all the bars,
        we can calculate the area of the largest rectangle that can be formed
        using each bar as the height of the rectangle.
        The area of the rectangle is equal to the height of the rectangle multiplied by the width 
        of the rectangle,
        which is the difference between the left and right boundaries plus one.

        8.We return the maximum area found in step 7.


        The time complexity of the algorithm is O(n) because it involves traversing the array         
        three times in the worst case.
        The space complexity of the algorithm is O(n) because we are storing two additional 
        arrays of size n.

        """

from collections import deque

def largestRectangleArea(A):
    
    n=len(A)
    
    if n==1:
        return A[0]
    
    left_smaller=[0]*n
    right_greater=[0]*n
    
    
    
    
    #finding the array of left immediate smaller element from the current
    stacks=deque()
    
    for i in range(n):
        while stacks and A[stacks[-1]]>=A[i]:
            stacks.pop()
        if stacks:
            left_smaller[i]=stacks[-1]+1
        else:
            left_smaller[i]=0
        stacks.append(i)
        
    #finding the array of right immediate larger element from the current
    stacks=deque()
    
    for i in range(n-1,-1,-1):
        while stacks and A[stacks[-1]]>=A[i]:
            stacks.pop()
        if stacks:
            right_greater[i]=stacks[-1]-1
        else:
            right_greater[i]=n-1
        stacks.append(i)
    
    
    max_val=0
    
    
    #calculate the max val
    
    for i in range(n):
        cur=A[i]*(right_greater[i]-left_smaller[i]+1)
        max_val=max(max_val,cur)
        
    return max_val
    
    