import sys
sys.stdin = open('input.txt','r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
# b = [list(map(int, input().split())) for _ in range(m)]

print(n)
print(a)
print(m)
# print(b)

for i in range(m):
  h, t, k = map(int, input().split())

  if t == 0:
    for _ in range(k):
      a[h-1].append(a[h-1].pop(0))

  else:
    for _ in range(k):
      a[h-1].insert(0, a[h-1].pop())

for x in a:
    print(x)

res = 0
s = 0
e = n-1

for i in range(n):
  for j in range(s, e+1):
    res += a[i][j]
  if i<n//2:
    s+=1
    e-=1
  
  else: # i >= n//2
    s-=1
    e+=1
    
print(res)


# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# m = int(input())

# for i in range(m):
#   x, y ,z = map(int, input().split())

#   if y == 0:
#     for _ in range(z): # 5회
#       a[x-1].append(a[x-1].pop(0))
#   else:
#     for _ in range(z):
#       a[x-1].insert(0, a[x-1].pop(0))  


# e, q = 0, n-1
# res = 0

# for i in range(n):

#   for j in range(e, q):
#     res += a[i][j]
#     e += 1
#     q -= 1
#   if  i >= n//2:
#     e -= 1
#     q
# print(res)
