def solution(n, t, m, p):
    answer = ''
    length = m * t      # m명이 하나의 숫자를 얘기하는 횟수가 t 번
    
    candidate = '0'
    num = 0
    alpha = 'ABCDEF'
    
    while len(candidate) < length : # length 길이보다 작을 때까지 n 진법으로 변환
        res= ''
        number = num
        while True:     #  자연수 number를 n진법으로 변환하는 반복문
            if number == 0:
                break
                
            if number % n:
                if number % n >= 10: # 10 ~ 15 값이면 alpha와 매핑
                    res += alpha[(number % n) % 10]
                else:
                    res+= str(number % n)
                    
            else:
                res+= '0'
            number //= n
        num +=1
        candidate += res[::-1] # 역순으로 담았다
    for i in range(p-1, length, m): 
        answer += candidate[i]
        
    return answer