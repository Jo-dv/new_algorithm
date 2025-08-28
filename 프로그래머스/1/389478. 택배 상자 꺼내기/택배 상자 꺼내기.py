def solution(n, w, num):
    answer = 1
    floor = n // w + (1 if n % w != 0 else 0)
    boxes = [[0] * w for _ in range(floor)]
    
    idx = 1
    exit = False
    flag = False
    
    for i in range(floor-1, -1, -1):
        for j in range(w-1 if flag else 0, -1 if flag else w, -1 if flag else 1):
            if idx == n+1:
                exit = True
                break
            boxes[i][j] = idx
            idx += 1
        flag = not flag
        if exit:
            break

    for i in range(floor):
        for j in range(w):
            if boxes[i][j] == num:
                for k in range(i):
                    if boxes[k][j] != 0:
                        answer += 1
                return answer

