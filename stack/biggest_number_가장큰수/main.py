import sys
sys.stdin = open('input.txt','r')


# num, m = map(int, input().split())
# print(num, m)

# # last in first out

# num = list(map(int, str(num)))

# stack = []
# for x in num:
#   while stack and m > 0 and stack[-1]< x:
#     stack.pop()
#     m-=1
  
#   stack.append(x)

# if m != 0:
#   stack = stack[:-m]
# res=''.join(map(str, stack))
# print(res)
num, m = map(int, input().split())
print(num, m)
#last in first out
num = list(map(int, str(num)))

stack = []
for x in num:
  while stack and m > 0 and stack[-1] < x:
    stack.pop()
    m-=1
  stack.append(x)

if m != 0:
  stack = stack[:-m]
res = ''.join(map(str, stack))
    
