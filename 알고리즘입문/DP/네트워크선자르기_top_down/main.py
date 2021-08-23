import sys
sys.stdin =open('input.txt','r')

def DFS(len):

  if dy[len]>0:
    return dy[len]

  if len ==1 or len == 2: #종착점에 온 경우
    return len
    
  else:
    dy[len]=DFS(len-1)+DFS(len-2) # 기록하지 않으면 시간이 굉장히 오래 걸리게 된다!
    return dy[len]


if __name__=="__main__":
  n=int(input())
  dy=[0]*(n+1) # 메모이제이션을 위한 리스트 . 인덱스를 1부터 사용하기 위해서 n+1을 곱해준다. 
  print(DFS(n))



