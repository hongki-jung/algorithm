import sys
sys.stdin = open('input.txt','r')

#8, 3
n, m = map(int, input().split())
print(n,m)

a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

print(a)
# lt = 0
# rt = 1
# tot = a[0]
# cnt = 0

while True:
  if tot<m:
    if rt<n:
      tot+=a[rt]
      rt+=1
    else:
      break

  elif tot == m:
    cnt+=1
    tot-=a[lt]
    lt+=1

  else:    # tot > m
    tot-=a[lt]
    lt+1
     
print(cnt)
# while True:
#   if tot < m:
#     if rt < n:
#       tot+=a[rt]









n, m = map(int, input().split())
print(n,m)

a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
  if tot > m:
    rt +=1
  
  if tot == m:
    cnt +=1
    rt +=1
  
