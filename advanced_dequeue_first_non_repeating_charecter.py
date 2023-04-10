from collections import deque

def solve(A):
    # @param A : string
    # @return a strings
    
    ########################My logic############################execution time:360 ms
        
        n=len(A)
    
        # edge case
        
        if n==0 or n==1:
            return A
        
        output_string=""
        
        freq=dict()
        
        queue=deque()
        
        for i in range(n):
            if A[i] not in freq:
                
                freq[A[i]]=1
                queue.append(A[i])
                output_string+=queue[0]       
            else:
                if queue:
                    if queue[0] == A[i]:
                        freq[A[i]]+=1
                        while queue and freq[queue[0]] >1:
                            queue.popleft()
                        
                        if not queue:
                            output_string+="#"
                        else:
                            output_string+=queue[0]
                    else:
                        freq[A[i]]+=1
                        output_string+=queue[0]
                else:
                    output_string+="#"
        return output_string
        
        ##################class logic ###################################
        
        # queue=deque()
        # output_string=""
        # freq=dict()
        # n=len(A)
        
        # if n==0 or n==1:
        #     return A
        
        # for i in range(n):
        #     if A[i] in freq:
        #         freq[A[i]]+=1
        #     else:
        #         freq[A[i]]=1
        #         queue.append(A[i])
                
        #     while queue and freq[A[i]]>1:
        #         queue.popleft()
        #     if queue:
        #         output_string+=queue[0]
        #     else:
        #         output_string+="#"
                
        # return output_string
        

print(solve("jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"))        
        
        