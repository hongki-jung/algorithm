import sys
sys.stdin = open('input.txt','r')
from collections import deque

# n, m = map(int, input().split())
# a = list(map(int, input().split()))

# print(n, m)
# # print(a)

# a.sort()
# print(a)

# p1 = 0
# p2 = 1
# cnt = 0
# max = 0

# while p1 < n and p2 < n:

#   if a[p1] + a[p2] <= m:
#     p2 +=1

#     if a[p1] + a[p2]> max:
#       max = a[p1]+a[p2]
#       cnt +=1

#     if p2 == n-1:
#       p1 += 1
#       p2 = p1+1

#   else:
#     p2+=1

# print(cnt)
    


  
# n, limit = map(int, input().split())
# p = list(map(int, input().split()))
# p.sort()

# p = deque(p)

# # cnt = 0 
# while p:
#   if len(p)==1:
#     cnt+=1
#     break

#   if p[0]+p[-1]> limit:
#     p.pop() # 탈출
#     cnt +=1
#   else:
#     p.popleft()
#     p.pop()
#     cnt+=1
# print(cnt)


n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)

# n, limit = map(int, input().split())
# p = list(map(int, input().split()))
# p.sort()
# p = deque(p)
# cnt
cnt = 0 

print(n, limit)
print(p)



while p :
  if len(p) == 1:
    p.pop()
    cnt +=1
    break;
  if p[0] + p[-1] > limit:
    p.pop()
    cnt +=1
  else:
    p.popleft()
    p.pop()
    cnt+=1
  

print(cnt)
# while p :
#   if len(p) == 1:
#     p.pop()
#     cnt+=1
#     break;
#   if p[0] + p[-1] > limit:
#     p.pop()
#     cnt +=1
#   else:
#     p.popleft()
#     p.pop()
#     cnt +=1

  
  


