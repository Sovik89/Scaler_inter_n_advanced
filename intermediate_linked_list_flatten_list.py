# You are given a nested list of integers nestedList. Each element is either an integer or 
# a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and 
# false otherwise.


# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, 
# the order of elements returned by next should be: [1,4,6].

# Constraints:
# The sum of integers in all cases does not exceed 1e5.
# The values of the integers in the nested list are in the range [-1e6, 1e6].


######################################### SOLUTION ########################################

 class NestedIterator:
    def __init__(self, nestedList):
        def flatten(nestedlst):# for recusively flattening the list
            res=[]#resultant list
            for i in nestedlst:
                if i.isInteger():
                    res.append(i.getInteger())
                else:
                    res.extend(flatten(i.getList()))
            
            return res
            
        self.i=0#index value
        self.l=flatten(nestedList)# flattened list
        self.n=len(self.l)#length of the list
            

    
    def next(self):
        temp = self.l[self.i]
        self.i+=1
        return temp
    
    def hasNext(self):
        return self.i<self.n