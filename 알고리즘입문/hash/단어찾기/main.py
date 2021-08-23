import sys
sys.stdin = open('input.txt','r')

n = int(input())
print(n)

# solve1 

# word = []
# word_check = []

# for i in range(n + n-1):
#   a = input()
#   if i < n:
#     word.append(a)
#   else:
#     word_check.append(a)

# for x in word:
#   if x not in word_check:
#     print(x)
  


p = dict()
for i in range(n):
  word = input()
  p[word]=1


print(p)

for i in range(n-1):
  word= input()
  p[word] = 0

for key, val in p.items():
  if val == 1:
    print(key)
    break
  # print(key, val)


