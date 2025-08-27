def solution(mats, park):
    answer = -1
    mats.sort(reverse=True)
    
    row = len(park)
    col = len(park[0])
    
    for mat in mats:
        for y in range(row-mat+1):
            for x in range(col-mat+1):
                if park[y][x] != "-1":
                    continue
                
                cnt = 0
                flag = False
                for i in range(mat):
                    for j in range(mat):
                        if park[y+i][x+j] == "-1":
                            cnt += 1
                        else:
                            cnt = 0
                            flag = True
                            break
                    if flag:
                        break
                            
                if cnt == mat*mat:
                    answer = max(answer, mat)
            
    return answer