import sys
sys.stdin =open('input.txt','r')

import heapq

n = int(input())
data =[]
for i in range(n):
  heapq.heappush(data, int(input()))

answer =0
while len(data) != 1:
  one = heapq.heappop(data)
  two = heapq.heappop(data)

  result = one + two
  answer+= result
  heapq.heappush(data, result)

print(answer)









