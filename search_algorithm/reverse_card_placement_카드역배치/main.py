import sys
sys.stdin = open('input.txt','r')


# tmp = []
# for i in range(1, 21):
#   tmp.append(i)

# for i in range(1,11):

#   a = list(map(int, input().split()))  
#   tmp = tmp[a[0]:a[1]:-1]

# print(tmp)
    


#선수지식 a , b 스와프
# a,b = map(int, input().split())
# print(a, b)
# a, b = b, a
# print(a, b)

# a = list(range(21))

# for _ in range(10): # _ :변수없이 반복
#   s, e = map(int, input().split())

#   for i in range((e-s+1)//2):
#     a[s+i], a[e-i] = a[e-i], a[s+i]

# a.pop(0)
# for x in a:
#   print(x, end=' ')



 

n = list(range(21))

for _ in range(10):
  a, s = map(int, input().split())
  # 5 10     5, 6, 7 , 8, 9,10 
  # 9 14.  9 10 11 12 13 14  14-9 = 5
  for i in range((s-a+1)//2):
    n[a+i], n[s-i] = n[s-i], n[a+i]

for x in n:
  print(x, end=' ')

