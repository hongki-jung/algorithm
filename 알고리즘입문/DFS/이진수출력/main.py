import sys
sys.stdin = open('input.txt','r')

# 10진수 -> 2진수로 변환


def DFS(v):
  if v == 0:
    return
  else:
    
    DFS(v//2)
    print(v%2, end='')

if __name__ == '__main__':
  n = int(input())
  DFS(n)
  