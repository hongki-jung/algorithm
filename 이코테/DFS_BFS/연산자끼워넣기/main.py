import sys
sys.stdin = open('input.txt','r')

num = int(input())
data = list(map(int, input().split()))
dic = {}
dic['add'], dic['sub'], dic['mul'], dic['div'] = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):       # 위치, 현재 값
    global min_value, max_value

    if i == num:    # 모든 연산자를 사용했을 때
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if dic['add'] > 0:
            dic['add'] -= 1	# + 수 차감
            dfs(i+1, now + data[i])		# 연산자를 모두 사용했을 때 나옴
            dic['add'] += 1	# + 복구, 위에서 나온 뒤 sub로 내려감
        if dic['sub'] > 0:
            dic['sub'] -= 1
            dfs(i+1, now - data[i])
            dic['sub'] += 1
        if dic['mul'] > 0:
            dic['mul'] -= 1
            dfs(i+1, now * data[i])
            dic['mul'] += 1
        if dic['div'] > 0:
            dic['div'] -= 1
            dfs(i+1, int(now/data[i]))
            dic['div'] += 1
print(dic)
dfs(1, data[0])

print(max_value)
print(min_value)