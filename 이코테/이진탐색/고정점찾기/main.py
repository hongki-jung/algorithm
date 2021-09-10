import sys
sys.stdin =open('input.txt','r')

# 고정점
# : 수열의 원소 중에서 그 값이
# 인덱스와 동일한 원소인 것을 말한다

# 고정점은 1개만 존재 
# 없다면 -1 출력



def binery_search(start ,end):


    if start > end:
      return None

    mid = (start + end) // 2 
    # 2

    if data[mid] == mid:
      return mid
      
    
    #.   1.         2
    if data[mid] < mid :
      return binery_search(mid+1 , end)


    else:
      return binery_search(start, mid-1)

if __name__ == "__main__":
  n = int(input())
  index = n
  data = list(map(int, input().split()))

  start = 0         
  end = len(data)-1   # 4 

  index = binery_search(start, end)

  if index == None:
    print("-1")
  else:
    print(index)
