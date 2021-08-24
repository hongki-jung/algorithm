from collections import deque
def solution(record):
    answer = []
    
    dq=[]
    user ={}
    for i in range(len(record)):
        record[i]=record[i].split()
    
    for content in record:
        if content[0] == 'Enter':
            user[content[1]]=content[2]
        elif content[0] == "Change":
            user[content[1]] = content[2]
    
    
    for content in record:
        if content[0] == 'Enter':
            dq.append(f"{user[content[1]]}님이 들어왔습니다.")
            
        elif content[0] == "Leave":
            dq.append(f"{user[content[1]]}님이 나갔습니다.")
    answer=dq
    return answer
    print('user', user)
    print('dq',dq)