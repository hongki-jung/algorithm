
import sys
sys.stdin = open('input.txt','r')


# n = int(input())
# a = list(map(int, input().split()))

# sum = 0
# for i,e in enumerate(a):
#   sum +=1
#   if i>1:
#     if a[i] == a[i-1]:
#       sum += 1
#     if a[i] == a[i-1] and a[i+1] == a[i]:
#       sum +=2
# print(sum)

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0 # 가중치

for x in a:
  if x ==1 :
    cnt +=1
    sum += cnt

  else:
    cnt = 0
print(sum)
