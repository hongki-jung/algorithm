import sys
sys.stdin = open('input.txt','r')
from collections import deque

MAX = 10000

ch=[0]*(MAX+1)
dis=[0]*(MAX+1)

#출발점, 도착점
#5. 14
n, m = map(int, input().split())

#  5
ch[n]=1 
dis[n]=0  # 출발점이니까 거리 0
dQ = deque()

dQ.append(n)  # 출발점 추가


while dQ:
  # now : 현재 지점
  now=dQ.popleft()
  if now == m:
    break
        #현재 지점-1, 현재 지점+1, 현재 지점+5
  for next in(now-1, now+1, now+5): # 3바뀌를 돈다 ==> next가 now-1이 되었다가, now+1이 되었다가, now+5가 된다(튜플값을 하나씩 탐색!)
    
    if 0 < next <= MAX:
      if ch[next]==0:
        dQ.append(next)
        ch[next]=1
        dis[next]=dis[now]+1 # 부모값



print(dis[m])