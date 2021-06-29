import sys
sys.stdin = open('input.txt','r')

def Count(capacity):
  # print(capacity)
  cnt = 1
  sum = 0
  for x in Music:
    if sum+x > capacity:
      cnt +=1
      sum=x
    else:
      sum+=x
  return cnt
      

# 9곡이 들어가는데 
# 같은 크기의 DVD 3개에 모든 동영상 녹화
n, m = map(int, input().split())

Music = list(map(int, input().split()))

lt = 1
rt = sum(Music)
res =0
while lt <=rt:
  mid=(lt+rt)//2

  if Count(mid) <= m:
    res = mid
    rt = mid-1

  else:
    lt = mid+1
# print(res)

# lf = 1
# rt = sum(Music)
# res = 0
# while lt<= rt:
#   mid=(lt+rt)//2

#   if Count(mid) <= m :
#     res = mid
#     rt = mid-1
#   else:
#     lt = mid+1