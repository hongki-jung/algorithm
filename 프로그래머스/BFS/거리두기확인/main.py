from collections import deque

# def bfs(place, x, y):
#     dx = [1, 0, -1, 0]
#     dy = [0, -1, 0, 1]
    
#     visited = [[False for _ in range(5)] for _ in range(5)]
    
#     q = deque()
#     visited[x][y] = True
#     q.append((x, y , 0))
    
    
#     while q:
#         px , py, dis = q.popleft()
        
#         if dis > 2:
#             continue # 거리 2 이상은 다 스킵
        
#         if dis != 0 and place[px][py] == 'P': # 거리 2이하고 자기자신이 아니면서 다른 P를 만났다
#             return False
        
#         for index in range(4):
#             nx = px + dx[index]
#             ny = py + dy[index]
            
#             if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False and place[nx][ny] != 'X':
#                 visited[nx][ny] = True
#                 q.append((nx, ny, dis+1))
                
#     return True            

# def check(place):
#     for i in range(5):
#         for j in range(5):
#             if place[i][j] == 'P':
#                 if bfs(place, i, j) == False:
#                     return False
#     return True        

# def solution(places):
#     answer = []
    
#     for place in places:
#         if check(place):
#             answer.append(1)
#         else:
#             answer.append(0)
#     return answer










def bfs(node,x, y):
    
    ch = [[0 for _ in range(5)] for _ in range(5)]
    dq = deque()
    dq.append((x, y))
    

    
    while dq:
        px, py = dq.popleft()
       
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0 ,1]
        
        if ch[px][py] > 2:
            continue
        
        if ch[px][py] != 0 and node[px][py] == 'P':
            return False
        
        
        for index in range(4):
            nx = px + dx[index]
            ny = py + dy[index]
           
            if 0 <= nx < 5 and 0 <= ny < 5 and node[nx][ny] != 'X' and ch[nx][ny] == 0:
                ch[nx][ny] = ch[px][py] + 1
                dq.append((nx, ny))
    
            
    return True
                    
        
def solution(places):
    answer = []
    # 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
    
    # 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
    
    # 위 그림처럼 자리 사이가 맨해튼 거리 2이고 사이에 빈 테이블이 있는 경우는 거리두기를 지키지 않은 것입니다.
    
    for place in places:
        dq = deque()
        p = list(place)
        
        node = [list(node) for node in p]
        
        
        
        for i in range(5):
            for j in range(5):
                if node[i][j] == 'P':
                    result = bfs(node,i, j)
                    # print("ch ?",ch)
                
                
        if result == False:
            answer.append(0)
        else:
            answer.append(1)
                
                                        
                    
    return answer