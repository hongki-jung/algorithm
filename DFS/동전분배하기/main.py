import sys
sys.stdin =open('input.txt','r')


def DFS(L):
  global res
  if L == n:
    cha = max(money) - min(money)
    if cha<res:

      # 중복값 체크
      tmp = set()
      for x in money:
        tmp.add(x)

      if len(tmp) == 3:
        res = cha
  else:
    for i in range(3):
      # coin array의 L번째에 있는 돈을 money array의 i번째 사람에게 주는 것이다.
      money[i]+=coin[L] 
      DFS(L+1)
      money[i]-=coin[L]
      
if __name__ =='__main__':
  n = int(input())
  coin = []
  res = 2147000000
  money=[0]*3
  for i in range(n):
    coin.append(int(input()))
  
  DFS(0)