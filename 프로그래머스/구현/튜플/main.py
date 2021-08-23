# 셀 수 있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플


# 원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수), 이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.

from collections import Counter

def solution(s):
    # s=s.split(',')
    s=s[1:-1]
    s=eval(s)
    s=sorted(s)
    
    array= []
    
 
    if len(s)==1:
        return s
    
    for i in range(len(s)-1):
        if i == 0:
            array.append(list(s[i])[0])
        
        a = s[i+1] - s[i]
        array.append(list(a)[0])
        
    return array