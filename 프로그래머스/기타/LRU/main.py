
# 사용자에게 빠르게 정보를 제공하기 위해 

# 사용하는 캐시에서 새로운 데이터가 발생했을 때, 
# 가장 오래전에 사용된 데이터를 제거하고 새로운 데이터를 삽입하는 알고리즘

# 1. 새로운 데이터가 들어온 경우
#   1) 캐시에 넣어준다
#   2) 캐시가 가득차있다면, 가장 오래된 데이터를 제거하고 넣어준다

# 2. 존재하는 데이터가 들어온 경우
#   1) 해당 데이터를 꺼낸 뒤
#   2) 가장 최근 데이터 위치로 보내준다


cache_Size = 5


user_data = [3, 7, 2]
cache = [1, 2, 3, 4, 5]

for data in user_data:
  # Miss! 
  if data not in cache:
    if len(cache) < cache_Size:
      cache.append(data)
    else:
      cache.pop(0)
      cache.append(data)
      
  # Hit ! 
  else:
    cache.pop(cache.index(data))
    cache.append(data)

print(cache)
# 결과 
# - 3은 캐시에 존재한다 따라서 최근 위치로 옮겨준다
# - 7은 새로운 데이터다. 하지만 그대로 넣어주면 cache_Size를 넘어가므로 가장 오래된 데이터 1을 제거하고 넣어준다  [2, 4, 5, 3 ,7]

# - 2는 캐시에 존재한다. 따라서 최근 위치로 옮겨준다. [ 4, 5, 3, 7, 2]