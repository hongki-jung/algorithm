import sys
sys.stdin = open('input.txt','r')

n = int(input())
dy=[0]*(n+1) # index 1부터 사용하기 위해서
dy[1]=1
dy[2]=2
for i in range(3, n+1):
  dy[i]=dy[i-1]+dy[i-2]  # i가 3이면 3미터짜리, 4면 4미터 짜리다.

print(dy[n])