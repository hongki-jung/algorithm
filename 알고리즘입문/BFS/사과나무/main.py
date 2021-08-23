import sys
sys.stdin = open('input.txt','r')
from collections import deque

#solution 1
# n = int(input())
# sum=0
# center, left, right = n//2, n//2, n//2

# for i in range(n):
#   a = list(map(int, input().split()))

#   if i < center:
#       print(left)
#       print(right)
#       for j in range(left, right+1):
#         sum+= a[j]

#       left-=1
#       right+=1


#   else:
#       print(left)
#       print(right)
#       for j in range(left, right+1):
#         sum+= a[j]

#       left+=1
#       right-=1

# print(sum)



dx = [-1,0,1,0]
dy=[0,1,0,-1] 
n = int(input())
a=[list(map (int, input().split())) for _ in range(n)]
print(a)
ch=[[0]*n for _ in range(n)]
sum=0

Q = deque()
ch[n//2][n//2] = 1
sum+=a[n//2][n//2]
Q.append((n//2, n//2))

L=0

while True:
  if L==n//2:
    break
    
  size=len(Q)

  for i in range(size):
    tmp=Q.popleft()
    for j in range(4):
      x=tmp[0]+dx[j]
      y=tmp[1]+dy[j]
      if ch[x][y]==0:
        sum+=a[x][y]
        ch[x][y]=1
        Q.append((x, y))
  L+=1

print(sum)