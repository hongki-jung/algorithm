import sys
sys.stdin = open('input.txt','r')

# 그래프 : 노드와 간선의 집합

n, m = map(int, input().split())

g=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
  a, b, c = map(int, input().split())
  g[a][b]=c

for i in range(1, n+1):
  for j in range(1, n+1):
    print(g[i][j], end=' ')
  print()

