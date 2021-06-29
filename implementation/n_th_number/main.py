# n 번째 수
import sys
sys.stdin=open("input.txt","rt")


# tcase : test Case 개수
# n : n개의 숫자로 이루어져있다.
# s : s번째 수부터
# e : e번째 수까지
# k : k번째로 나타나는 숫자

T = int(input())

for t in range(T):
  n, s, e, k = map(int, input().split())
  a = list(map(int, input().split()))
  
  a=a[s-1:e]  #s번째부터 e번째까지 자르기
  a.sort()
  print("#%d %d" %(t+1, a[k-1]))






# for t in range(T):
#   n, s, e, k= map(int, input().split())
#   a = list(map(int, input().split()))













