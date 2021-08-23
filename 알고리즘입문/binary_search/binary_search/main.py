import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

# c.sort()
# tmp = 0
# for i, j in enumerate(c):
#   if b == j:
#     tmp = i
# print(tmp)

lt = 0 
rt = n-1

while lt <= rt:
  mid=(lt+rt)//2
  if a[mid] == m:
    print(mid+1)
    break;
  
  elif a[mid] > m:
    rt=mid-1
    
  else:
    lt=mid+1
  


