import sys
sys.stdin = open('input.txt','r')

def DFS(L, sum):

  global result

  if L > result:
    return

  if sum > back :
    return

  if sum == back:
    if L < result:
      result = L
      

  else:
    for i in range(n):
      DFS(L+1, sum+a[i])


if __name__ == '__main__':

  # 동전 종류의 개수 
  n = int(input())

  # n개의 동전의 종류
  a = list(map(int, input().split()))

  back = int(input())
  result = 2147000000
  
  DFS(0, 0)
  print(result)













# def DFS(L, sum):

#   global res
#   if L > res:
#     return

#   if sum > m:
#     return

#   if sum == m:
#     if L < res:
#       res = L

#   else:
#     for i in range(n):
#       DFS(L+1, sum+a[i])

# if __name__ == "__main__":

#   n = int(input())  # 동전의 종류개수
#   a = list(map(int, input().split())) # 동전의 종류
#   m = int(input()) # 거스름 돈

#   res=2147000000
#   a.sort(reverse=True)  # 시간단축을 위해서

#   DFS(0, 0)
#   print(res)