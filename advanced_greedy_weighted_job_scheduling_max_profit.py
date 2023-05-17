import heapq


def solve(A):
    A.sort()
    heap=[]
    cp,mp = 0,0                           # cp->current profit, mp-> max-profit
    for s,e,p in A:
        while heap and heap[0][0]<=s:
            _,tmp = heapq.heappop(heap)
            cp = max(cp,tmp)
        heapq.heappush(heap,(e,cp+p))
        mp = max(mp,cp+p)
            
    return mp   
    



# print(solve([    
#     [1,2,50],
#     [3,5,20],
#     [6,9,100],
#     [2,100,200]
# ]))

# print(solve([    
#     [3,6,3],
#     [6,7,8],
#     [3,7,7],
#     [3,10,9],
#     [7,8,7],
#     [6,6,3],
#     [1,5,7],
#     [2,5,1],
#     [5,7,8]
# ]))


            
        
    