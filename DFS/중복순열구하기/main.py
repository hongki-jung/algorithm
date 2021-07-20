import sys
sys.stdin = open('input.txt','r')


# solution1
# n, m = map(int, input().split())

# a = []

# for x in range(1, n+1):
#   a.append(x)

# cnt = 0

# for x in a:
#   for y in a:
#     print(x ,y)
#     cnt += 1
    
# print(cnt)
# # print(a)

def DFS(L):
  global cnt
  if L == m: # 하나의 중복순열 완성 
    for j in range(m):
      print(res[j], end=' ')
    print()
    cnt+=1
  else:
    # 가닥 분기
    for i in range(1, n+1):
      res[L]=i
      DFS(L+1)



if __name__ == "__main__":
  n, m = map(int, input().split())
  res=[0]*m
  cnt =0
  DFS(0)
  print(cnt)