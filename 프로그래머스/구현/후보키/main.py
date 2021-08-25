# from itertools import chain, combinations



# # 모든 부분집합을 구하는 함수
# def get_all_subset(iterable):
#   s = list(iterable)
#   return chain.from_iterable(combinations(s, r) for r in range(len(s)+ 1))

# # 부분집합 중에서 유일성을 만족하는 부분집합을 구하는 함수
# # => 어떤 리스트가 들어오면 그 리스트의 모든 부분집합을 구한다.
# def get_all_unique_subset(relation):
#   subset_list = get_all_subset(list(range(0, len(relation[0]))))

#   unique_list = []

#   # 특정 부분집합 . subset_list의 요소가 1개일 땐 한 번 , 2개일 땐 두 번 반복
#   for subset in subset_list:
#     unique = True
#     row_set = set()

#     # relation 리스트의 모든 요소를 확인하자 !
#     for i in range(len(relation)):
#       row = ' ' 
#       for j in subset:
#         # j를 만족하는 
#         row += relation[i][j] +'.'
#       if row in row_set:
#         unique =False
#         break
#       row_set.add(row)
    
#     if unique:
#       unique_list.append(subset)
#   return unique_list

    
# def solutino(relation):
#   answer =[]
#   unique_list = get_all_unique_subset(relation)

#   unique_list = sorted(unique_list, key=lambda x : len(x))

#   answer_list = []
#   for subset in unique_list:
#     subset = set(subset)
#     check = True

#     for j in answer_list:
#       if j.issubset(subset):
#         check = False
    
#     if check == True:
#       answer_list.append(subset)
#   return len(answer_list )


from itertools import chain, combinations

def get_all_subset(iterable):
  s = list(iterable)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# 부분집합 중에서 유일성을 만족하는 (열의 쌍)을 구하는 함수
# => 어떤 리스트가 들어오면 그 리스트의 모든 부분집합을 구한다

def get_all_unique_subset(relation):
  subset_list =get_all_subset(list(range(0, len(relation[0]))))

  unique_list = []

  for subset in subset_list:
    unique = True
    row_set = set()

    # 유일성 체크 
    # relation 리스트의 모든 요소들을 확인할 것
    for i in range(len(relation)):
      row = ' '
      for j in subset:
        row+=relation[i][j] + '.'

      if row in row_set:
        unique = False
        break
      row_set.add(row)

    if unique:
      unique_list.append(subset)

  return unique_list


def solution(relation):

  unique_list = get_all_unique_subset(relation)
  unique_list = sorted(unique_list , key= lambda x : len(x))

  answer_list = []
  # 최소성 체크
  for subset in unique_list:
    subset = set(subset)
    check = True

    for j in answer_list:
      if j.issubset(subset):
        check = False

    if check == True:
      answer_list.append(subset)

  return len(answer_list)