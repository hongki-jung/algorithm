import sys
sys.stdin= open("input","txt")

# 카드 n 장   
# k번째로 큰 수 출력 

n, k = map(int, input().split())
a = list(map(int, input().split()))

res = set() # 자료구조 set은 중복을 제거한다
for i in range(n):
  for j in range(i+1, n):
    for m in range(j+1, n):
      res.add(a[i]+a[j]+a[m])

res = list(res)

res.sort(reverse=True)  #내림차순
print(res[k-1])


# res = set()
# for i in range(n): # 10
#   for j in range(n+1, n):
#     for m in range(j+1, n):
#       res.add(a[i]+a[j]+a[m])

