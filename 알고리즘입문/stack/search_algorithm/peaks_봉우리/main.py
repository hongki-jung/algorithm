import sys
sys.stdin = open('input.txt','r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

n = int(input())
print(n)

a = [list(map(int, input().split())) for _ in range(n)]


a.insert(0, [0]*n)
a.append([0]*n)

# a.insert(0, [0]*n)
# a.append([0]*n)

for x in a:
  x.insert(0,0)
  x.append(0)
  
cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):

# a[1][1]  a[1][2]  a[1][3] .....
  #    a [i+dx[k]] [j+dy[k]]
    if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
      cnt += 1

  # if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
  #   cnt +=1 

print(cnt)


# for i in range(1, n+1):
#   for j in range(1, n+1):

#     if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
#       cnt +=1
# print(cnt)
    

