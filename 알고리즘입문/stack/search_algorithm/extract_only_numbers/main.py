import sys
sys.stdin = open('input.txt','r')

# txt =input()

# tmp1 =[]
# for i in str(txt):
#   tmp1.append(i)

# print(tmp1)
# tmp2 = []
# for a in tmp1:

#   if type(a) is int:
#     print('hi')
#     tmp2.append(a)

# print(tmp2)   



# s = input()
# res = 0
# for x in s:
#   if x.isdigit():
#     res = res*10 + int(x)
  
# print(res)

# cnt = 0
# for i in range(1, res+1):
#   if res%i == 0:  #나누어 떨어지면 약수! 
#     cnt +=1
# print(cnt)





# 다시 풀어봄

s = input()
print(s)

res = 0
cnt = 0

for i in s:
  
  if i.isdigit():
    res = res * 10 + int(i)


for i in range(1, res+1):
  if res % i == 0 :
    cnt += 1

print(res)
print(cnt)

