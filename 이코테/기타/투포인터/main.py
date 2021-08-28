
# 합이 5인 연속하는 두 수를 찾는문제

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합M
data = [1, 2, 2, 3, 2, 5] # 전체 수열


one = 0
two = 0
cnt = 0
print(" data[one: two+1]?", data[one: two+2])
while one < len(data)-1:

  new_data = sum(data[one: two+1])
  if new_data < m:
    two +=1 
  elif new_data == m:
    two +=1
    cnt +=1
  else:
    one +=1

print("cnt ",cnt)









# 합이 5인 연속하는 두 수를 찾는문제

# n = 5 # 데이터의 개수 N
# m = 5 # 찾고자 하는 부분합M
# data = [1, 2, 2, 3, 2, 5] # 전체 수열

# count = 0
# interval_sum = 0
# end =0

# # start를 차례대로 증가시키며 반복
# for start in range(n):

#   # end를 가능한 만큼 이동시키기
#   while interval_sum < m and end <n:
#     interval_sum += data[end]
#     end+=1
  
#   # 부분합이 m일 때 카운트 증가
#   if interval_sum == m:
#     count +=1
#   interval_sum -= data[start]

# print(count)