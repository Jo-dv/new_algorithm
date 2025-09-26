from collections import deque

def search(y, x, visited, maps, row, col):
    dq = deque([(y, x)])
    result = int(maps[y][x])
    visited[y][x] = True
    
    while dq:
        cy, cx = dq.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            my, mx = cy + dy, cx + dx
            if 0 <= my < row and 0 <= mx < col and not visited[my][mx] and maps[my][mx] != "X":
                visited[my][mx] = True
                dq.append((my, mx))
                result += int(maps[my][mx])
                
    return result, visited

def solution(maps):
    answer = []
    row = len(maps)
    col = len(maps[0])
    visited = [[False] * col for _ in range(row)]
    maps = [list(maps[i]) for i in range(row)]
    
    for y in range(row):
        for x in range(col):
            if not visited[y][x] and maps[y][x] != "X":
                result, visited = search(y, x, visited, maps, row, col)
                answer.append(result)
    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer