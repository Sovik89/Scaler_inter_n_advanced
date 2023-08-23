import sys
sys.setrecursionlimit(10**6)
from collections import deque


def dfs(i,j,mat,length):
        if mat[i][j]==0:
            return length

        left=right=top=down=0

        if mat[i][j]:
            if j-1>=0:
                left=dfs(i,j-1,mat,length+1)
            if i-1>=0:
                top=dfs(i-1,j,mat,length+1)
            if j+1<len(mat[0]):
                right=dfs(i,j+1,mat,length+1)
            if i+1<len(mat):
                down=dfs(i+1,j,mat,length+1)

        return min(left,right,top,down)

def updateMatrix(mat):
        row=len(mat)
        col=len(mat[0])
        op_mat=[[0]*col for _ in range(row)]
        my_queue=deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j]!=0:
                    my_queue.append([i,j])

        while my_queue:
            r,c=my_queue.popleft()
            dist_0=dfs(r,c,mat,0)
            op_matrix=dist_0

        return op_matrix

print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))