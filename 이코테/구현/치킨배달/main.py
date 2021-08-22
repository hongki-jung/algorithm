import sys
sys.stdin =open('input.txt','r')

from itertools import combinations





if __name__ == "__main__":
  
  n, m = map(int, input().split())
  # 0 빈집 , 1집, 2 치킨집
  data = [list(map(int, input().split())) for _ in range(n)]
  print("data? ",data)
  
  house = []
  chicken = []
  for i in range(n):
    for j in range(n):
      if data[i][j] == 2:
        chicken.append((i, j))
      elif data[i][j] == 1:
        house.append((i, j))

  # 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
  candidates =list(combinations(chicken, m))
  print("house? ",house)
  print("candidates",candidates)
  
  # 치킨 거리의 합을 계산하는 함수
  def get_sum(candidate):
    result = 0

    # 모든 집에 대하
    for hx, hy in house:
      print("hx, hy",hx, hy)
      # 가장 가까운 치킨집을 찾자
      temp =1e9
      for cx, cy in candidate:
        print("cx, cy? ",cx, cy)
        temp = min(temp, abs(hx- cx) + abs(hy -cy))
      #가장 가까운 치킨집까지의 거리를 더하기
      result += temp
    #치킨 거리의 합 반환
    return result

  # 치킨 거리의 합의 최소를 찾아서 출력
  result = 1e9
  for candidate in candidates:
    result =min(result, get_sum(candidate))
  
  


  # print("chicken_cb ?",chicken_cb)
  # print("chiken ?",chiken)