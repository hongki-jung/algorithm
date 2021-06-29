import sys
sys.stdin = open('input.txt','r')

n = int(input())
# print(n)


body = []

# for i in range(n):
#   s, e = map(int, input().split())
#   body.append((s, e))

# body.sort(key=lambda x : (x[0], x[1]), reverse=True)

# print(body)
# max =0 
# cnt =0 

# for i, j in body:
#   if j > max:
#     max = j
#     cnt +=1
# print(cnt)
# print(Athletic)


for _ in range(n):
  
  s, e = map(int, input().split())
  body.append((s, e))
  body.sort(reverse=True)

tmp = 0
cnt = 0
print(body)
for i, j in body:
  # print(j)
  if j > tmp:
    # print(j)
    tmp = j
    cnt += 1

print(cnt)
  
  




# print(body)






