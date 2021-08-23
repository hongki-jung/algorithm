import sys
sys.stdin = open('input.txt','r')

a = input()
b = input()
















# solution 1
# str1 = dict()
# str2 = dict()
# for x in a:
#   if str1.get(x):
#     str1[x] +=1 
#   else:
#     str1[x] = 1

# for x in b:
#   if str2.get(x):
#     str2[x] +=1 
#   else:
#     str2[x] = 1

# for x in b:
#   if str2.get(x):
#     str1[x] -=1 


# solution 2

# str1 = dict()
# str2 = dict()
# for x in a:
#   str1[x]=str1.get(x, 0)+1

# for x in b:
#   str2[x] = str2.get(x, 0)+1

# for i in str1.keys():
#   if i in str2.keys():
#     if str1[i] != str2[i]:
#       print("No")
#       break
#     else:
#       print("No")
#       break
# else:
#   print("Yes")


# solution3

sH = dict()

for x in a:
  sH[x] = sH.get(x, 0)+1

for x in b:
  sH[x] = sH.get(x, 0)-1

for x in a:
  if sH.get(x) > 0:
    print("No")
    break

else:
  print("Yes")




