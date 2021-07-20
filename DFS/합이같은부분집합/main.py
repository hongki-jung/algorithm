import sys
sys.stdin = open('input.txt','r')






















# solution 1
  #   level
# def DFS(L, sum):
#   if L == n:
#     if sum == (total-sum):
#       print("YES")
#       sys.exit(0) # 프로그램 종료 
    
#    else:
#      DFS(L+1, sum+a[L])  # a[L]이라는 원소를 사용하겠다.
#      DFS(L+1, sum)       # a[L]이라는 원소를 사용하지 않겠다.


# if __name__ == "__main__":

#   n = int(input())
#   a = list(map(int, input().split()))
#   total = sum(a)
#   DFS(0, 0)
#   print("NO")



# solution 2 리팩토링 
def DFS(L, sum):
  if sum > total//2:
    return

  if L==n:
    if sum==(total-sum):
      print("YES")
      sys.exit(0) # 프로그램 종료 
    
  else:
    DFS(L+1, sum+a[L])  # a[L]이라는 원소를 사용하겠다.
    DFS(L+1, sum) # a[L]이라는 원소를 사용하지 않겠다.


if __name__ == "__main__":

  n = int(input())
  a = list(map(int, input().split()))
  total = sum(a)
  DFS(0, 0)
  print("NO")