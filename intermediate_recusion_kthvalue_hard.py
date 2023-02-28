# Problem Constraints
# 1 <= A <= 105

# 0 <= B <= min(2A - 1 - 1 , 10^18)

# If easy code is used in this program we will have time limit exceeded issue. we will go with levels


# taking the case of
            # Row 1: 0
            # Row 2: 01
            # Row 3: 0110
            # Row 4: 01101001


            #   parent              0  
            #          (A,B)  =   (1,0)
            #                     0        1    kid
            #                   (2,0)     (2,1)

            #                  0       1         1         0   grandkid
            #             (3,0)      (3,1)      (3,2)      (3,3)
                                             
            #         0      1     1     0      1     0    0     1 greater grand kid
            #         (4,0) (4,1) (4,2) (4,3) (4,4) (4,5) (4,6)  (4,7)
                     
                    #  suppose at row 4 and at 7th index    stacked 1
                    #  parent  coordinate will be A-1,B//2-->3,3 stacked 2
                    #  parent  coordinate will be A-1,B//2--->2,1 stacked 3
                    #  parent  coordinate will be A-1,B//2--->1,0 return value =0

                    #  at stacked3 @(2,1)--->A=2, B=1 is odd value , so kid =1 -parent value
                    #  at stacked2 @(3,3)--->A=3, B=3 is odd value , so grandkid =1 -kid  value
                    #  at stacked1 @(4,7)--->A=4, B=7 is odd value , so greater grandkid =1 -grandkid  value


def solve(A,B):    
        
        if A==1 or B==0: # base cond.n. in every row where index=0, return value =0
            return 0    
        elif A>1 and B==1:
            return 1 
        x=solve(A-1,B//2)# this will go to value and coordinate of parent elemnt        
        
        if B%2 ==0: # if the kid is at left index or even index, it will be same as parent elemnt
                return x
        else: #if the kid is at left index or even index, it will (1- parent) elemnt
                return 1-x
        
        
print(solve(4,4))
print(solve(3,0))