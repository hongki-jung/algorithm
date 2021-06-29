import sys
sys.stdin = open('input.txt','r')

# solution 1  nlog(n) - 좋지않은 풀이
# n = int(input())
# a = list(map(int, input().split()))
# n2 = int(input())
# b = list(map(int, input().split()))

# newlist = a+b
# newlist.sort()



n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 내가 잘못 접근
# p1, p2 = 0, 0
# c = []

# for i in range(len(a+b)):
#   if a[p1] == 0:
#     c =b[p2:]

#   else:
#     if a[p1] < b[p2]:
#       if p1 < len(a):
        
#         c.append(a[p1])
#         p1 += 1
#     else:
#       if p2 < len(b):
#         p2 +=1
#         c.append(b[p2])

# print(c)


p1, p2 = 0, 0
c = []

while p1 < n and p2 < m:
  if a[p1] <= b[p2]:
    c.append(a[p1])
    p1+=1
  else:
    c.append(b[p2])
    p2 +=1

if p1 <n:
  c = c+a[p1:]
if p2 <m:
  c = c+b[p2:]

for x in c:
  print(x, end=' ')

# p1, p2 = 0, 0
# c = []

# while p1< n and p2 <m:
#   if a[p1] <= b[p2]:
#     c.append(a[p1])
#     p1+=1
#   else:
#     c.append(b[p2])
#     p2 +=1
# if p1<n:
#   c = c+a[p1:]
# if p2 < m:
#   c = c+b[p2:]






# ex

# 1 3 5
# 2 3 6 9



# c = []

# while p1 < n and p2 < m:
#   if a[p1]< b[p2]:
#     c.append(a[p1])
#     p1 +=1
#   elif a[p1] > b[p2]:
#     c.append(b(p2))
#     p2 +=1

#   else:
#     p1+=1

# if p1 > n:
#   c = c + a[p1:]
# if p2 >m:
#   c = c + b[p2:]
# print(c)



# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# p1 , p2 = 0, 0
# c = []

# while p1 < n and p2 < m:
#   if a[p1] <= b[p2]:
#     c.append(a[p1])
#     p1 += 1
  
#   else:
#     c.append(b[p2])
#     p2 += 1

# if p1 < n:
#   c = c + b[p1:]

# if p2 < m:
#   c = c+ b[p2:]





