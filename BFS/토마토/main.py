import sys
sys.stdin = open('input.txt','r')
from collections import deque
n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dQ = deque()
cnt = 0

board = [list(map(int, input().split())) for _ in range(m)]

dis = [[0]*n for _ in range(m)]


for i in range(m):
  for j in range(n):
    if board[i][j] == 1:
      dQ.append((i, j))

while dQ:
    tmp = dQ.popleft()
    for i in range(4):
      xx = tmp[0]+dx[i]
      yy = tmp[1]+dy[i]
      # print(xx)
      # print(yy)
      if 0<= xx < m and 0<= yy <n :
        if board[xx][yy] == 0:
         
          dis[xx][yy]= dis[tmp[0]][tmp[1]] +1
          board[xx][yy] = 1
          dQ.append((xx, yy))
print(cnt)

flag =1
for i in range(m):
  for j in range(n):
    if board[i][j] == 0:
      flag = 0
result=0
if flag==1:
  for i in range(m):
    for j in range(n):
      if dis[i][j] > result:
        result = dis[i][j]
  print(result)
else:
  print(-1)