
# 내 풀이법
# n , k  = map(int, input().split())

# y =[]
# cnt = 0

# 이렇게 해야 n까지 돈다
# for i in range(1, n+1):
#   if(n%i == 0):
#     y.append(i)

# if len(y) < k:
#   print(-1)
# else:
#   y.sort()
#   print(y[k-1])
#   print(y)


# 좋은 풀이 
n , k  = map(int, input().split())
cnt = 0

for i in range(1, n+1):
  if n%i ==0:
    cnt +=1
  if cnt == k:
    print(i)
    break

else:
  print(-1)


  