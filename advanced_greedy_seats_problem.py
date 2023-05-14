class Solution:
	# @param A : string
	# @return an integer
    def seats(self, A):
        # A is string 
        #O/P is an integer of sum of possible moves
        
        mod=(10**7)+3
        
        occupied_seats=[]
        
        for i in range(len(A)):
            if A[i]=="x":
                occupied_seats.append(i)
                
        
        total_occupied=len(occupied_seats)
        
        if total_occupied ==1 or total_occupied == 0:
            return 0
        
        mid=(total_occupied)//2
        median_seat=occupied_seats[mid]
        ans=0
        
        for j in range(total_occupied):
            ans+=(abs(occupied_seats[j]-median_seat)-abs(mid-j))%mod
            
        return ans%mod
