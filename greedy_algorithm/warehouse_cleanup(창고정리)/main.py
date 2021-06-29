import sys
sys.stdin = open('input.txt','r')

n = int(input())
a = list(map(int, input().split()))
m = int(input())


a.sort()

# print(max(a))
# print(min(a))


# min(a)

# for i in range(50):
#   a.sort()
#   a[a.index(max(a))] = a[a.index(max(a))]-1
#   a[a.index(min(a))] = a[a.index(min(a))]+1
  
  

# c = max(a)-min(a)
# print(c)
  

for i in range(m):
  a[0] = a[0]+1
  a[n-1] = a[n-1]-1
  a.sort()

c = a[n-1] - a[0]

# print(a[m])
# c = a[m-1]- a[0]
print(c)



