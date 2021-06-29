import sys
sys.stdin = open('input.txt','r')


n = int(input())


# print(n)
# tmp = 0
# a = [list(map(int, input().split())) for _ in range(n-1)]
# print(a)
# for i, j in enumerate(a):
#   print(a[i])

# 그리디 - 정렬 후 선택
# meeting = []

# for i in range(n):
#   s, e = map(int, input().split())
#   meeting.append((s, e))
  

# meeting.sort(key=lambda x : (x[1], x[0])) # x : 매개변수
# print(meeting)
# # [(2, 3), (1, 4), (3, 5), (4, 6), (5, 7)]
# et = 0
# cnt = 0 
# for s, e in meeting:
#   if s>=et:
#     et = e
#     cnt +=1

# print(cnt)



tmp = []
for i in range(n):
  s, e = map(int, input().split())
  tmp.append((s, e))

tmp.sort(key=lambda x : (x[1], x[0]))

et = 0
cnt = 0

for s, e in tmp:
  
  if s >= et:
    et = e
    cnt += 1
print(tmp)
print(cnt)