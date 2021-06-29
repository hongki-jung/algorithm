
import sys
sys.stdin = open('input.txt','r')

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)

print(n)
print(a)

seq=[0]*n

for i in range(1,n+1):
  for j in range(n):
    if a[i] == 1 and seq[j] == 0: # 자기자리 찾아서 들어감
      seq[j] = i
      break;
    elif seq[j] == 0:             # 빈자리
        a[i] -= 1
  

for x in seq:
  print(x, end=' ')








# 1보다 큰 수 5개
# 2보다 큰 수 3개 
# 3보다 큰 수 4개
# 4보다 큰 수 없음
# 5보다 큰 수 2개
# 6보다 큰 수 1개
# 7보다 큰 수 1개
# 8보다 큰 수 0개 


