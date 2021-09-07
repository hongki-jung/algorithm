import sys
sys.stdin =open('input.txt','r')

# 도현이의 집 N개가 수직선 위에 있다
# X1, X2 , ..... Xn


# 공유기 C개 설치 예정
n, c = list(map(int, input().split()))

# 전체 집의 좌표정보 입력받기
array = []
for _ in range(n):
  array.append(int(input()))
array.sort() # 이진탐색 수행을 위한 정렬 수행

start = 1 # 가능한 최소거리(min gap)
end = array[-1] - array[0] # 가능한 최대거리(max gap)

result =0

while (start <= end):
  mid = (start + end)//2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미한다.
  value = array[0]  # 1

  count = 1  
  #현재의 mid값을 이용해 공유기를 설치
  for i in range(1, n): #앞에서부터 차근차근 설치

    if array[i] >= value+mid:
      value = array[i]
      count += 1

  if count >= c : # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
    start = mid +1
    result = mid # 최적의 결과를 저장
  else:
    # C개 이상의 공유기를 설치할 수 없는 경우 , 거리 감소
    end =mid- 1
print(result)