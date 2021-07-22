import sys
sys.stdin = open('input.txt','r')

from collections import deque



# solution 1
# dx = [-1 , -1, 0, 1 , 1 , 1, 0, -1]
# dy = [0 , 1 , 1 , 1, 0, -1, -1, -1]

# def BFS():
#   while dQ:
#     now = dQ.popleft()
#     for i in range(8):
#       xx = now[0]+dx[i]
#       yy = now[1]+dy[i]
#       if 0 <= xx < n and 0 <= yy < n and board[xx][yy]== 1:
#         board[xx][yy]=0
#         dQ.append((xx, yy))


# if __name__ == "__main__":

#   dQ = deque()
#   n=int(input())
#   board = [list(map(int, input().split())) for _ in range(n)]
#   print(board)
#   cnt=0

#   res=[]

#   for i in range(n):
#     for j in range(n):
#       if board[i][j] == 1:
#         cnt+=1
#         dQ.append((i, j))
#         BFS()
     

# print(cnt)      




dx = [-1 , -1, 0, 1 , 1 , 1, 0, -1]
dy = [0 , 1 , 1 , 1, 0, -1, -1, -1]
n = int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt =0
Q=deque()

for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      board[i][j]=0
      Q.append((i, j))
      while Q:
        tmp= Q.popleft()
        for k in range(8):
          x = tmp[0]+dx[k]
          y = tmp[1]+dy[k]
          if 0<=x<n and 0<=y<n and board[x][y]==1:
            board[x][y]=0
            Q.append((x,y))
      cnt+=1
print(cnt)