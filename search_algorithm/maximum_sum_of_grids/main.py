import sys
sys.stdin = open('input.txt','r')

# n=int(input())
# print(n)

# sum1 = 0
# sum2 = 0
# sum3 = 0
# sum4 = 0

# row = 0       # 가로최대 
# column = 0    # 세로최대
# ldiagonal = 0 # 왼쪽 대각선
# rdiagonal = 0 # 오른쪽 대각선
# cycle1 =0
# cycle2 =4

# for i in range(n):
#   k = list(map(int, input().split()))
  
#   for i in k:
#     sum1 += i
#     if sum1 > row:
#       row = sum1
#   sum1=0    
  

#   for j in range(5):
#     sum2 += k[j]
#     if sum2 > column:
#       column = sum2


#   if cycle1<5:
#     ldiagonal += k[cycle1]
#     rdiagonal += k[cycle2]
#     cycle1+=1
#     cycle2 -=1

    
# print(row)
# print(column)
# print(ldiagonal)
# print(rdiagonal)

n = int(input())

#이렇게 하면 한줄  읽어서  리스트화
# a = [list(map(int, input().split()))]

a = [list(map(int, input().split())) for _ in range(n)]

# a = [list(map(int, input().split())) for _ in range(n)]

largest=-2147000000
for i in range(n):
  sum1 = sum2 = 0
  for j in range(n):
    sum1+=a[i][j]
    sum2+=a[j][i]
  
  if sum1>largest:
    largest=sum1
  if sum2>largest:
    largest=sum2

# for i in range(n):
#   sum1 = sum2 = 0
#   for j in range(n):
#     sum1+=a[i][j]
#     sum2+=a[j][i]
#   if sum1 > largest:
#     largest = sum1
#   if sum2 > largest:
#     largest = sum2


sum1 = sum2 =0
for i in range(n):
  sum1 += a[i][i]
  sum2 += a[i][n-i-1]
if sum1>largest:
  largest=sum1
if sum2>largest:
  largest=sum2

# sum1 = sum2 =0
# for i in range(n):
#   sum1 += a[i][i]
#   sum2 += a[i][n-i-1]
# if sum1 > largest:
#   largest = sum1
# if sum2 > largest:
#   largest = sum2

print(largest)