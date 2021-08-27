def solution(files):
    answer = []
    file_name_list = []
    
    for file in files:
        
        temp_list = []
        head = ''
        number = ''
        tail =''
        
        check = False
        for i in range(len(file)):
            

            if file[i].isdigit(): 
                number += file[i]
                
                check = True

            elif not check:
                head += file[i]
                
            
            else:
                tail = file[i:]
                break
                
    
        
        file_name_list.append((head, number, tail))    
    
        
    sort = sorted(file_name_list, key = lambda x: (x[0].lower(), int(x[1])))
        
    for i in range(len(sort)):
        sort[i] = ''.join(sort[i])
            
         
    return sort