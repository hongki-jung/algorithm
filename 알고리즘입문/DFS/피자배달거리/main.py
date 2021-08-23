import sys
sys.stdin = open('input.txt','r')


def DFS(L, s):
  global res
  if L == m:
    # for x in cb:
    #   print(x, end=' ')
    # print()
    
    # 도시의 피자거리 
    sum=0
    for j in range(len(hs)): # 집 개수만큼 돈다
      x1=hs[j][0] #집의 좌표
      y1=hs[j][1]   
      dis=2147000000  
      for x in cb:
        x2 = pz[x][0] # 피자집의 좌표
        y2 = pz[x][1] 
        dis=min(dis,abs(x1-x2)+ abs(y1-y2))
      sum+=dis
    if sum<res:
      res=sum

  else:
    for i in range(s, len(pz)):
      cb[L]=i
      DFS(L+1, i+1)


if __name__ == '__main__':
  n, m = map(int, input().split())
  # print(n, m)

  board = [list(map(int, input().split()))for i in range(n)] 
  hs = []       # 집 좌표
  pz = []       # 피자집 좌표
  cb = [0]*m    # 조합
  res=2147000000
  for i in range(n):
    for j in range(n):
      if board[i][j]==1:
        hs.append((i, j))
      elif board[i][j]==2:
        pz.append((i, j))
  DFS(0, 0)