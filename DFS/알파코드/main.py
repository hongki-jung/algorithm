import sys
sys.stdin = open('input.txt','r')


def DFS(L, P):
  global cnt
  if L==n:
    cnt+=1
    # for j in range(P):  
    #   print(res[j], end=' ')
    # print()

    for j in range(P):  
      print(chr(res[j]+64), end='')
    print()

       
  else:
    for i in range(1, 27):
      if code[L]==i:    # i가 2일때 참
        res[P]=i
        DFS(L+1, P+1)
      elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:    # 이 부분 주의 23 , 14
        res[P]=i
        DFS(L+2, P+1)   # L+2 : 두자리 숫자니까




if __name__ == '__main__':
  code = list(map(int, input()))
  n=len(code) # 5
  code.insert(n, -1)   # 마지막에 -1 추가 . 이부분 주의 . 주석 처리하고 해보자
  res=[0]*(n+3)
  cnt=0
  DFS(0, 0)
  print(cnt)