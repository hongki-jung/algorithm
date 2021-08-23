import re
from itertools import permutations
from collections import deque

def solution(expression):
    expression = re.split('([-+*])',expression)
    results = []
    
    operators = list(permutations(['-','+','*'], 3))
    
    for operator in operators:
        exp = expression[:]
        
        for op in operator: # ['-','+','*']
            print("op ????", op)
            while op in exp:
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1]+ op + exp[idx+1]))
                del exp[idx:idx+2]
        results.append(abs(int(exp[0])))

    print("results?",results)
    return max(results)



# for i in expression:
#         if i.isdecimal()==True:
#             temp+=i
#         else:
#             array.append(temp)
#             array.append(i)
#             temp =""
            
#     array.append(temp)