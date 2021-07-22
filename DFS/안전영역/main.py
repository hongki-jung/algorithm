import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1 ,0, -1]

def DFS(x, y, h):
  # 퍼져나간다
  ch[x][y]=1
  for i in range(4):
    xx = x+dx[i]
    yy = y+dy[i]
    if 0<= xx< n and 0 <= yy < n and  ch[xx][yy]==0 and board[xx][yy] > h:
      DFS(xx, yy, h)

if __name__ == "__main__":

  n = int(input())  # 5 
  cnt = 0   # 안전영역의 개수 
  res = 0   # 최종 정답
  board = [list(map(int, input().split())) for _ in range(n)]

  # 높이
  for h in range(100): # 0 ~ 99 안전영역 개수
    ch=[[0]*n for _ in range(n)]
    cnt=0
    for i in range(n):
      for j in range(n):
        if ch[i][j]==0 and board[i][j] > h :
          cnt+=1  # 안전영역 찾았다! 
          DFS(i, j, h)

    res=max(res, cnt)
    if cnt == 0:  # 참 없음 .. 안전영역 없음
      break
print(res)