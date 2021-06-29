import sys
sys.stdin = open('input.txt','r')

# from collections import deque


# print(n)
# print(a)

# a.sort()
# tmp = []
# print(a)
# while a:

#   if a[0] < a[-1]:
#     a.pop(0)
#     tmp.append('L')
    
  
#   else:
#     tmp.append('R')
#     a.pop()


# print(tmp)

# n = int(input())
# a = list(map(int, input().split()))

# lt = 0
# rt = n-1
# last = 0

# res = "" # 여기다 문자열 넣을 거
# tmp = []

# while lt <= rt:
#   if a[lt]>last:
#     tmp.append((a[lt], 'L'))
  
#   if a[rt]>last:
#     tmp.append((a[rt], 'R'))
  
#   tmp.sort()

#   print(tmp)

#   if len(tmp) == 0:
#     break

#   else:
#     res = res + tmp[0][1]
#     last = tmp[0][0]

#     if tmp[0][1] == 'L':
#       lt += 1
#     else:
#       rt -= 1
#   tmp.clear()


# print(len(res))
# print(res)
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0

res = "" # 여기다 문자열 넣을 거
tmp = []

print(n)
print(a)

while lt <= rt:
  if a[lt] > last:
    tmp.append((a[lt],'L'))

  if a[rt] > last:
    tmp.append((a[rt],'R'))
  
  
  if len(tmp) == 0:
    break;
  else:
    
    # 하나씩 추가한다.
    res = res + tmp[0][1]
    last = tmp[0][0]

    if tmp[0][1] =='L':
      lt+=1
    else:
      rt-=1

  tmp.clear()

print(len(res))
print(res)