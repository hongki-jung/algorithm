
import sys
sys.stdin = open('input.txt','r')

# n = int(input())

# solution 1
# for index in range(n):

#   i = input()
#   if i == i[::-1]:
#     print('#'+str(index)+' '+'Yes')

#   else:
#     print('#'+str(index)+' '+'NO')
    

n = int(input())
for i in range(n):
  s = input()
  s = s.upper()

  size = len(s) 
  for j in range(size//2):
    if s[j] != s[-1-j]:
      print("#%d NO" %(i+1))
      break
  else:
      print("#%d YES" %(i+1))


    
