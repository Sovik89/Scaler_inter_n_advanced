def towerofHanoi(A):
    result = []
    def toh(N,source,intermediate,destination):
        if N == 0:
            return 
        toh(N-1,source,destination,intermediate) # Move n-1 discs from source to temp step by step
        result.append([N,source,destination]) # Move n discs from source to destination
        toh(N-1,intermediate,source,destination) # Move n-1 discs from temp to destination step by step
        
    toh(A,1,2,3)
    
    return result


print(towerofHanoi(3)) 