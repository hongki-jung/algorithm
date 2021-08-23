import sys
sys.stdin = open('input.txt','r')


# num =int(input())

# def digit_sum(x):
#   sum = 0

#   x = str(x)
  
#   for i in range(len(x)):
#     sum += i

n = int(input())
a = list(map(int, input().split()))

def degit_sum(x):
    sum=0

    # solution 1
    while x>0:
      sum+=x%10
      x=x//10     #10으로 나눈 몫
    
    # solution 2   문자열 활용
    # for i in str(x):
    #   sum += int(i)
    #   print(i, end=' ')
    # print(i)

    return sum


max= -2147000000
for x in a:
  tot = degit_sum(x)
  if tot>max:
    max=tot
    res=x
  
print(res)

# n = input()
# a = list(map(int, input().split))

# def digit_sum(x):
#   sum =0 
#   for i in str(x):
#     sum +=i
#   return sum

# max = -21213
# for x in a:
#   tot = degit_sum(x)
#   if tot > max:
#     max = tot
#     res = x



# n = input()
# a = list(map(int, input().split))

# def digit_sum(x):
#   sum = 0
#   for i in str(x):
#     sum += i
#   return sum

# max = -23132
# for x in a:
#   total = degit_sum(x)
#   if tot > max:
#     max = tot
#     res = x








    


