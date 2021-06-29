import sys
sys.stdin = open('input.txt','r')



e = 0
q = 5
cnt = 0
arr = []

# for i in range(7):
#   for j in range(e, q):
#     if j < 7 :
#       arr.append(a[i][j])
#       e+=1
#       q+=1
  

board = [list(map(int, input().split())) for _ in range(7)]
for i in range(3):
  for j in range(7):
    tmp= board[j][i:i+5]
    if tmp == tmp[::-1]: # reverse
      cnt +=1
    for k in range(2):
      if board[i+k][j] != board[i+5-k-1][j]:
        break;
    else:
      cnt+=1
print(cnt)

board = [list(map(int, input().split()))for _ in range(7)]
for i in range(3):
  for j in range(7):
    tmp = board[j][i:i+5]
    if tmp == tmp[::-1]:
      cnt +=1
    for k in range(2):
      if board[i+k][j] != board[i+5-k-1][j]:
        break;
      else:
        cnt+=1
