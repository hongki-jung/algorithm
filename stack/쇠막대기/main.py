import sys
sys.stdin = open('input.txt','r')


# s = input()
# stack = []
# cnt = 0
# for i in range(len(s)):
#   if s[i]=='(':
#     stack.append(s[i])

#   else:
#     stack.pop()
#     if s[i-1] == '(':
#       # 레이저
      
#       cnt+= len(stack)
#     else:
#       #쇠막대기 끝
#       cnt+=1
# print(cnt)
      

s = input()
stack = []
cnt = 0

print(s)

for x in range(len(s)):

  if s[x] == '(':
    stack.append('(')
  else:

    stack.pop()
    if s[x-1] == '(':
      cnt += len(stack)
    else:
      cnt+=1
      

print(cnt)















