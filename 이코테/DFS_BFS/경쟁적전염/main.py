import sys
sys.stdin = open('input.txt','r')

from collections import deque

def bfs():
  global cnt, time
  while virus and time < s:
    
    
    cnt +=1
    if cnt % s == 0:
      time +=1
    # x , y : 좌표
    # z 바이러스 종류
    xx, yy, zz = virus.popleft()
    
    for i in range(4):
      nx = xx +dx[i]
      ny = yy +dy[i]
      if 0 <= nx < n and 0<= ny < n and board[nx][ny] == 0:
        board[nx][ny] = zz
        virus.append((nx ,ny, zz))



if __name__ == "__main__":
  n, k = map(int, input().split())
  board = [list(map(int, input().split())) for i in range(n)]

  s, x, y = map(int, input().split())
  print("s, x, y ?",s, x, y)
  dx = [1, 0, -1, 0]
  dy = [0, -1, 0, 1]

  virus = deque([])

  for i in range(n):
    for j in range(n):
      if board[i][j] != 0:
        virus.append((i, j, board[i][j]))
  
  k_array = [] 
  time = 0
  cnt =0
  for i in range(k):
    k_array.append(i)

  bfs()
  
  print("board ??>",board)
  
  if board[x-1][y-1] == 0:
    print(0)
  else:
    print(board[x-1][y-1])