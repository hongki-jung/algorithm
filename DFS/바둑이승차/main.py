import sys
sys.stdin = open('input.txt','r')


def DFS(L, sum):


  global max
  # 합계(sum)가 제한된 무게(c) 보다 큰 경우 
  if sum > c:
    return

  if L == n:
    if sum > max:
      max = sum

  else:
    # 제한된 무게(c) 보다 작은 합계 중 최대값 찾기
    DFS(L+1, sum+a[L])
    DFS(L+1, sum)

if __name__ == '__main__':
  
  c , n = map(int, input().split())
  print(c, n)
  a = []
  max = -2147000000
  for _ in range(n):
    a.append(int(input()))
  print(a)
  DFS(0, 0)
  print(max) 


























# bad solution 1
# def DFS(L, sum):
#   global max
#   if L == 4 :
#     if sum < c and sum > max:
#         max = sum

#   else:
#     DFS(L+1, sum + a[L])
#     DFS(L+1, sum)


# if __name__ == '__main__':

#   c, n = map(int, input().split())
#   a = []
#   # print(c, n)
#   sum = 0
#   max = 0

#   for _ in range(n):
#     k = int(input())
#     a.append(k)
  
#   DFS(0,0)
#   print(max)
 


# solution2
# def DFS(L, sum, tsum):
#   global result

#   if sum+(total-tsum)< result: 
#     return.

#   if sum > c:
#     return

#   if L == n:
#     if sum> result :
#       result = sum
#   else:
#     DFS(L+1, sum+a[L], tsum+a[L])
#     DFS(L+1, sum, tsum+a[L])


# if __name__ == '__main__':
#   c, n = map(int, input().split())
#   a = [0]*n

#   result = -2147000000
#   for i in range(n):
#     a[i] = int(input())
#     total = sum(a)
#   DFS(0, 0, 0)
#   print(result)