import sys
sys.stdin = open('input.txt','r')

def DFS(L, s, sum):
  global cnt

  if L == k: # 조합완성
    if sum%m == 0: # 나눠 떨어지는지 체크
      cnt+=1
  else:
                  # 리스트 a에서 가져오는 것
    for i in range(s, n):
      DFS(L+1, i+1, sum+a[i])




if __name__ == '__main__':
  # n 개중에서 k 개를 뽑는다
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  m = int(input())
  cnt = 0
  DFS(0, 0, 0) 
  print(cnt)