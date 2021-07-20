import sys
sys.stdin = open('input.txt','r')


# L 은 동전 종류 , sum 금액
def DFS(L, sum):
  global cnt
  if sum >T:
    return

  if L == k:
    if sum==T:
      cnt+=1

  else:
    #               4
    for i in range(cn[L]+1):
      DFS(L+1, sum+(cv[L]*i))

if __name__ == '__main__':
  T = int(input()) # 지폐금액
  k = int(input()) # 동전의 가지 수 

  cv = list() # 동전금액
  cn = list() # 동전개수

  for i in range(k):
  # a: 동전금액 , b: 동전개수
    a, b = map(int, input().split()) 
    cv.append(a)
    cn.append(b)

  cnt = 0
  
  DFS(0, 0)
  print(cnt)