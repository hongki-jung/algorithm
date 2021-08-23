import sys
sys.stdin = open('input.txt','r')




# T: 상담 완료에 걸리는 날 수
# P: 상담했을 때 받을 수 있는 금액






# solution 1

def DFS(L, sum):
  global max
  if L > n:
    return
  if L == n:
    if sum > max:
      max = sum
  else:
      DFS(L+tp[L][0], sum+tp[L][1])
      DFS(L+1, sum)

if __name__ == '__main__':

  n = int(input())
  tp =[]

  max = -21470000
  for _ in range(n):
    a, b = map(int, input().split())
    tp.append((a, b))
  
  print(tp)
  DFS(0, 0)
  print(max)



# solution 2

# def DFS(L, sum):
#     global res
#     if L == n+1:  #종료지점
#       if sum > res:
#         res = sum
#     else:
#       if L+T[L]<= n+1:  #  이 부분이 중요
#         DFS(L+T[L], sum+P[L])
#       else:
#         DFS(L+1, sum)


# if __name__ == "__main__":
#   n = int(input())
#   T = list()
#   P = list()
#   for i in range(n):
#     a, b = map(int, input().split())
#     T.append(a)
#     P.append(b)
#   res=-2147000000
#   T.insert(0, 0)  #인덱스를 날짜로 하기 위해서 
#   P.insert(0, 0)  #인덱스를 날짜로 하기 위해서 
#   DFS(1, 0)
#   print(res)