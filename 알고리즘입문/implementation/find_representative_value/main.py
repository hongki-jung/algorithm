# import sys
# sys.stdin=open("input.txt","r")

# n = int(input())
# a = list(map(int, input().split()))

# tmp = 0

# for i in range(len(a)):
#   tmp+=a[i]

# average = int(tmp/len(a))
# initNumber = float('inf')

# for i in range(len(a)):
#   if(abs(average-a[i]) < initNumber):
#     initNumber = abs(average-a[i])

#   if(abs(average-a[i]) == initNumber):
#     print(a[i-1])

# print(initNumber)

import sys

sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

ave = (sum(a) / n) + 0.5
ave = int(ave)
# ave = round(sum(a)/n)
# round() 소수첫째자리에서 반올림. 단, round_half_even
# sum() : list의 모든 값을 합친다.

min = 2124999900

#idx : 학생번호 (인덱스 값)
# x : 성적 (값)
for idx, x in enumerate(a):
    tmp = abs(x - ave) # abs() 절대값을 구해주는 함수
    if tmp < min:
        min = tmp
        score = x      # 점수 값
        res = idx + 1

    # = else if
    elif tmp == min:
        if x > score:   # x : 현재학생의 점수 ,score : 이전의 답
            score = x
            res = idx + 1

print(ave, res)

# a = list(map(int, input().split()))
# ave = (sum(a)/n) + 0.5
# min = 212032
# for idx, x in enumerate(a):
#   tmp = abs(x-ave)  # abs()
#   if tmp < min:
#     min = tmp
#     score = x
#     res= idx +1

#   elif tmp == min:
#     if x> score:
#       score =x
#       res = idx+1
