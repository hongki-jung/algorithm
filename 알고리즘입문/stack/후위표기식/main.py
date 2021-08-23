import sys
sys.stdin = open('input.txt','r')

a = input()
stack = []

res = ''


print(a)

for x in a:
  if x.isdecimal():
    res += x

  elif x == '(':
    stack.append('(')

  elif x == '*' or x == '/':
    while stack and (stack[-1] == '*' or stack[-1] == '/'):
      res+=stack.pop()
    stack.append(x)

  elif x == '+' or x == '-':
    while stack and stack[-1] != '(':
      res+= stack.pop()
    stack.append(x)

  elif x == ')':
    if stack and stack[-1] != '(':
      res += stack.pop()
    stack.pop()

while stack:
  res+=stack.pop()

print(res)














# for x in a:
#   # x 가 10진수면 참
#   if x.isdecimal():
#     res += x
#   else:
#     if x=='(':
#       stack.append(x)
#     elif x == '*' or x=='/':
#       while stack and (stack[-1]=='*' or stack[-1] == '/'):
#         res+= stack.pop()
#       stack.append(x)
#     elif x == '+' or x == '-':
#       while stack and stack[-1] != '(':
#         res += stack.pop()
#       stack.append(x)

#     elif x==')':
#       while stack and stack[-1] != '(':
#         res += stack.pop()
#       stack.pop()
    
# while stack:
#   res += stack.pop()
  
# print(res)