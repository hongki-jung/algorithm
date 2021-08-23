import sys
import heapq as hq


sys.stdin = open('input.txt','r')

a = []
while True:
  n = int(input())

  if n == -1:
    break
  if n == 0:
    if len(a) == 0:
      print(-1)
    else:
      print(hq.heappop(a))  # 루트 노드 값을 pop한다 .
  
  else:
    # push
    hq.heappush(a, n) #list a 에 n 값을 넣어준다



