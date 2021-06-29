import sys

sys.stdin = open('input.txt','r');



# for i in a:
#   isPrime(i)
# ch = [0]*len(a)

# 소수인지 체크
# def isPrime(x):
#   if x % 2 == 0:
#           # 소수
#  뒤집는 함수
# def reverse(x)

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
  res = 0
  while x > 0:
    t = x%10
    res = res*10+t
    x = x//10     # 10으로 나눈 몫
  return res

 
# def reverse(x):
#   res = 0
#   while x > 0:
#     t = x % 10          
#     res = res * 10 + t    
#     x = x//10 # 10으로 나눈 몫
#   return res



# def reverse(x):
#   res = 0
#   while x > 0 :
#     t = x % 10
#     res = res *10 +t
#     x = x//10
#   return res

def isPrime(x):
  if x == 1:
    return False
  
  for i in range(2, x//2+1):
    if x%i==0:
      return False
  else:
    return True

for x in a:
  tmp = reverse(x)  
  if isPrime(tmp):
    print(tmp, end=' ')
