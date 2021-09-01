import sys
sys.stdin = open('input.txt','r')
from collections import deque


def turn(direction_index, direction):
  
  if direction == 'L':
    direction_index = (direction_index - 1)%4
  else:
    direction_index = (direction_index + 1)%4
  
  return direction_index

def simulate():
  
  direction_index = 0
  
  x, y = 1, 1
  data[x][y]=2
  snake = [(x, y)]
  
  global time 
  while True:

    nx = x + dx[direction_index]
    ny = y + dy[direction_index]
    print("nx ny",nx,ny)
    if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:

      if data[nx][ny] == 0:
        
        px, py= snake.pop(0)
        data[px][py] = 0
        snake.append((nx, ny))
        data[nx][ny] = 2
        
      else:
        
        snake.append(((nx, ny)))
        data[nx][ny] = 2
    else:
      time+=1
      break

    
    x , y = nx, ny
    time+=1
    for j in range(direction_info_count):
      if time == direction_info[j][0]:
        direction_index = turn(direction_index, direction_info[j][1])    
    
    # if direction_info and time == direction_info[0][0]:
    #   print("direction_info[0][0]?? ",direction_info[0][0])
    #   if direction_info[0][1] == 'D':
    #     # 오른쪽
    #     direction_index=turn(direction_index, 'R')
    #   else:
    #     # 왼쪽
    #     direction_index=turn(direction_index, 'L')

    #   direction_info.popleft()

  return time