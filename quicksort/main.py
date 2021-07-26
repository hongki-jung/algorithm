# 퀵정렬
def qsort(lt, rt):
  if lt<rt:
    pos=lt # 분할된 영역의 시작 지점 
    pivot = arr[rt]
    for i in range(lt, rt):
      if arr[i]<=pivot:
        arr[i], arr[pos] = arr[pos], arr[i]
        pos+=1
    arr[rt], arr[pos] = arr[pos], arr[rt]
    # return 

            # pos가 축이 있는 지점
    Qsort(lt, pos-1)
    
    Qsort(pos+1, rt)



if __name__ == "__man__":
  arr=[45, 21 ,23, 36, 15, 67, 11, 60, 20, 33]
  print("Before sort : ",end='')
  print(arr)
  Qsort(0, 9)
  print("After sort : ", end='')
  print(arr)