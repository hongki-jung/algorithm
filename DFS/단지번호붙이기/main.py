import sys
sys.stdin = open('input.txt','r')

dx=[-1, 0, 1, 0]
dy=[0, 1 ,0, -1]

def DFS(x, y):
  global cnt
  cnt+=1 # 집 좌표가 넘어오면 카운팅
  board[x][y] = 0 # 방문하면 지워주자
  for i in range(4):
    xx = x+dx[i]
    yy = y+dy[i]

    if 0<= xx <n and 0 <= yy < n and board[xx][yy]==1:  # 가고자 하는 지점이 집이어야지 뻗어나간다
      DFS(xx, yy) 





if __name__== "__main__":
  n = int(input())
  board = [list(map(int, input())) for _ in range(n)]
  res=[] # 한 단지의 집의 개수
  for i in range(n):
    for j in range(n):
      if board[i][j]==1:
        cnt=0  # 새로 단지가 발견될 때마다 cnt를 0으로 초기화
        DFS(i, j)
        res.append(cnt)
  res.sort()
  print(res)
