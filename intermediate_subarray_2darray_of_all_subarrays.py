def solve(self, A):
        sub_array_repo=list() #2D Array for all sub Array
        n=len(A)
        for i in range(0,n):
            for j in range(i,n):
                temp_list=list()
                for k in range(i,j+1):
                    temp_list.append(A[k])
                sub_array_repo.append(temp_list)
                
        
        return sub_array_repo