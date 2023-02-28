# example A=5,B=3     ===> every 3rd person gets killed, next person starts with index=1
 
# 1st 2nd 3rd 4th 5th --> 3̶r̶d̶  4th 5th 1st 2nd  (y)                 # round 1 or stack 1,A=5
#                               becomes
#                             1st 2nd 3rd 4th (x)

# 1st 2nd 3rd 4th  --> 3̶r̶d̶  4th  1st 2nd  (y)                     # round 2 or stack 2,A=4
#                               becomes
#                             1st 2nd 3rd  (x)    

# 1st 2nd 3rd  --> 3̶r̶d̶   1st 2nd       (y)               # round 3 or stack 3,A=3
#                         becomes
#                        1st 2nd    (x)    



#             derived formula---> y=(x+B)%A   where B==3 and A is A of current stack
#               if y becomes 0 then assign value of A

def solve(A,B):
    # After the first person (B-th from the beginning) is killed, 
    # A-1 persons are left. So we call Josephus(A – 1, B) to get the 
    # position with A-1 persons. But the position returned by 
    # Josephus(A – 1, B) will consider the position starting from B%A + 1. 
    # So, we must make adjustments to the position returned by Josephus(A – 1, B). 

    # Time Complexity : O(A)
    # Space Complexity : O(A)
    def josephus(A,B):
        if A==1:
            return 1
        x=josephus(A-1,B)
        y=(x+B)%A
        if y==0:
           y = A
        return y
    
    return josephus(A,B)

# Firstly, the person at position 2 is killed, then the person at position 4 is killed,
# then the person at position 3 is killed. So the person at position 1 survives.
print(solve(4,2))# O/P:1

# Firstly, the person at position 3, then the person at position 1 is killed, 
# then the person at position 5 is killed. Finally, the person at position 2 is killed. 
# So the person at position 4 survives.
#print(solve(5,3))# O/P:4
        
        
            
        
        

        
    