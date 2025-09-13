def solution(rows, columns, queries):
    answer = []
    arr = [[c for c in range(1, columns+1)] for r in range(rows)]
    num = 1
    for r in range(rows):
        for c in range(columns):
            arr[r][c] = num
            num += 1
    
    for query in queries:
        r1, c1, r2, c2 = map(lambda i: i-1, query)
        temp = [i[:] for i in arr]
        result = rows * columns + 1
        
        for c in range(c1+1, c2+1):
            temp[r1][c] = arr[r1][c-1]
            result = min(result, temp[r1][c])
            
        for r in range(r1+1, r2+1):
            temp[r][c2] = arr[r-1][c2]
            result = min(result, temp[r][c2])
            
        for c in range(c2-1, c1-1, -1):
            temp[r2][c] = arr[r2][c+1]
            result = min(result, temp[r2][c])
            
        for r in range(r2-1, r1-1, -1):
            temp[r][c1] = arr[r+1][c1]
            result = min(result, temp[r][c1])
            
        arr = temp
        answer.append(result)
        
    return answer