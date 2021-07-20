import sys
# sys.stdin = open('input.txt','r')

def DFS(v):
  # 노드값이 7까지 있다
  if v > 7:
    return # 7보다 크면 종료시킨다.
  else:
    # 전위순회
    # print(v, end='')  # 자기 본연의 일
    # DFS(v*2)  # 왼쪽 자식노드 호출
    # DFS(v*2+1) # 오른쪽 자식 노드 호출
    
    # 자기 본연의 일 먼저 하고 왼쪽 자식의 일을 처리한 후 빽해서 오른쪽 일을 한다.

    # 중위순회
    # DFS(v*2)  # 왼쪽 자식노드 호출
    # print(v, end='')  # 자기 본연의 일
    # DFS(v*2+1) # 오른쪽 자식 노드 호출

  #왼쪽먼저 다 처리하고 백하고 돌아와서 본연의일(부모)의 일을 한다. 그다음에는 오른쪽 일을 처리한다.

    # 후위순회
    DFS(v*2)  # 왼쪽 자식노드 호출
    DFS(v*2+1) # 오른쪽 자식 노드 호출
    print(v, end=' ')  # 자기 본연의 일

if __name__ == "__main__":
  # ch = [0]*(3)
  # print(ch)
  DFS(1)