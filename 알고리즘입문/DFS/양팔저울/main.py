import sys
sys.stdin = open('input.txt','r')



def DFS(L, sum):
  global res
  if L==n:
    if 0<sum<=s:
      res.add(sum) # 음수는 안봐도 된다. 저울 - 대칭구조 . 

  else:
    DFS(L+1, sum+G[L])
    DFS(L+1, sum-G[L])
    DFS(L+1, sum)

# K : 추의 개수
# 모든 추 무게의 합 : S 

if __name__ == "__main__":
  n = int(input())
  G=list(map(int, input().split()))

  s=sum(G)
  res=set() # 집합, 중복제거
  DFS(0, 0)
  print(res)
  print(s-len(res))
  # s (총 개수) , res (측정가능한 것들)
  # s-len(res) : 측정 불가능한 것들의 개수