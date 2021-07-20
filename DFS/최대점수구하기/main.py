import sys
sys.stdin = open('input.txt','r')

# solution 1
# def DFS(L, t, sum):
#   global max
#   if sum > m:
#     return
#   if L == n:
#     if t > max:
#       max = t
#   else:
#     for i in range(n):
#       DFS(L+1, t +tmp_array[i][0], sum + tmp_array[i][1])
#       DFS(L+1,t,sum)

# if __name__ == '__main__':
# #문제개수,제한시간
#   n , m = map(int, input().split())

#   tmp_array =[]

#   for i in range(n):
#     a, b = map(int, input().split())
#     tmp_array.append((a, b))

#   max = -2146000
#   DFS(0 ,0, 0)
#   print(max)


# solution2
# 1, 2 ,3...문제 / 풀었을 경우 얻는 점수 / 쓴 시간
    #  문제 , 총점, 시간 
def DFS(L, sum, time):
    global res
    if time >m:
      return

    if L == n:
      if sum>res:
        res=sum
    else:
      DFS(L+1, sum+pv[L], time+pt[L])
      DFS(L+1, sum, time)


if __name__ == "__main__":
  n, m = map(int, input().split())
  pv=list() # 점수
  pt=list() # 시간 
  for i in range(n):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)
  res= -21470000000
  DFS(0, 0, 0)
  print(res)