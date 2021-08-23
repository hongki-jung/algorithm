

# 병합정렬 = 분할정복 !

def Dsort(lt, rt):
  if lt < rt:
    mid=(lt+rt)//2
    Dsort(lt, mid)    # 왼쪽 노드 영역
    Dsort(mid+1, rt)  # 오른쪽 노드 영역

    # 본연의 일 <- 왼쪽 노드와 오른쪽 노드의 일을 다 끝내고 처리 
    p1=lt
    p2=mid+1
    tmp=[]

    # 두 리스트를 합치는 부분 
    while p1 <= mid and p2 <= rt:
      if arr[p1] < arr[p2]:
        tmp.append(arr[p1])
        p1+=1
      else:
        tmp.append(arr[p2])
        p2+=1
    #p1이 남아있으면
    if p1<=mid:
      tmp = tmp+arr[p1:mid+1]

    #p2가 남아있으면 
    if p2<=rt:
      tmp = tmp+arr[p2:rt+1]
    
    #복사
    for i in range(len(tmp)):
      arr[lt+i]=tmp[i]



if __name__ == "__main__":
  arr =[23, 11, 45, 36, 15, 67, 33, 21]
  print("Before sort : ", end="")
  print(arr)
  Dsort(0, 7)
  print() 
  print("After sort : ", end="")
  print(arr)

