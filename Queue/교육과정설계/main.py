import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


n , m = map(int, input().split())
print(n, m)   # m 이 찾는값!?!

Q = [(x, y) for x, y in enumerate(list(map(int, input().split())))]
Q=deque(Q)
print(Q)
cnt =0
while True:

  # 맨앞의 환자보다 위급한 환자가 있는 경우
  # => 뒤로 보낸다  
  if any(Q[0][1] < x[1] for x in Q):
    cur = Q.popleft()
    Q.append(cur)
  
  # 맨앞의 환자보다 위급한 환자가 없는 경우
  else:
    cur = Q.popleft()
    cnt+=1
    if cur[0] == m:
      break

print(cnt)












# Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# print(Q)
# Q = deque(Q)


# cnt = 0

# while True:
#   cur = Q.popleft()

#   if any(cur[1] < x[1] for x in Q):
#     Q.append(cur)
#   else:
#     cnt +=1
#     if cur[0] == m:
#       break;

# print(cnt)