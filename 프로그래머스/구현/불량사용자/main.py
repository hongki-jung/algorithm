from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    candidates = [[]]
    
    p_u=list(permutations(user_id, len(banned_id)))
    print("p_u ",p_u)
    for b_id in banned_id:
        new_candidates = []
        
        for u_id in user_id:
            if len(u_id) != len(b_id):
                continue
            check = True
            for i in range(len(u_id)):
                
                # u_id[i]와 b_id[i]가 다르고, b_id[i]가 *이 아닌 경우 
                # 이 부분이 핵심이다. 이부분을 생각해낼 수 있어야 한다. 다행히도 그렇게 어렵지 않다!
                if b_id[i] != '*' and u_id[i] != b_id[i]:
                    check = False
                    break
                    
            if check:
                for c in candidates:
                     
                    if u_id not in c:
                        
                        print("c  ",c )
                        print("[u_id] ", [u_id])
                        print("c + [u_id] ",c + [u_id])
                        
                        new_candidates.append(c + [u_id])
                        print("new_candidates ",new_candidates)
                        print()
        candidates = new_candidates
        print('hi candidates',candidates)
        print()
        
    for c in candidates:
        if set(c) not in answer:
            answer.append(set(c))

    return len(answer)