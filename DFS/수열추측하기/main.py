import sys
import itertools as it
sys.stdin = open('input.txt','r')


# solution 1
# def DFS(L, sum):
#   if L == n and sum == f:
#     for x in p:
#       print(x, end=' ')
#     print()
#     sys.exit(0)
#   else:
#     for i in range(1, n+1):
#       if ch[i] == 0:
#         ch[i]=1
#         p[L]=i
#         DFS(L+1, sum+(p[L]*b[L]))
#         ch[i]=0



# if __name__ == '__main__':
#   # n 가장 윗줄에 있는 숫자의 개수
#   # f 가장 밑에 줄에 있는 수
#   n, f= map(int, input().split())
#   p =[0]*n    # 순열
#   b = [1]*n   # 1331 이런식으로 이항계수 초기화 
#   ch = [0]*(n+1) # 중복방지용 체크배열
  
#   for i in range(1, n):
#     b[i]= b[i-1]*(n-i)//i

#   DFS(0, 0)


# 라이브러리 사용한 풀이
n, f = map(int, input().split())
b = [1]*n
cnt=0
for i in range(1, n):
  b[i]=b[i-1]*(n-i)/i
a=list(range(1, n+1))

print(a)

for tmp in it.permutations(a):
  sum=0
  for L, x in enumerate(tmp):
    sum+=(x*b[L])
  if sum == f:
    for x in tmp:
      print(x, end=' ')
    break;