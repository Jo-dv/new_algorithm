from collections import deque

def search_block(target, board):
    size = len(board)
    visited = [[False] * size for _ in range(size)]
    shapes = []
    
    for i in range(size):
        for j in range(size):
            if board[i][j] == target and not visited[i][j]:
                visited[i][j] = True
                dq = deque([(i, j)])
                shape = [(i, j)]
                
                while dq:
                    y, x = dq.popleft()
                    
                    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        my, mx = y + dy, x + dx
                        
                        if 0 <= my < size and 0 <= mx < size and not visited[my][mx] and board[my][mx] == target:
                            visited[my][mx] = True
                            dq.append((my, mx))
                            shape.append((my, mx))
                            
                shapes.append(normalize(shape))
    
    return shapes

def normalize(shape):
    min_y = 51;
    min_x = 51;
    
    for y, x in shape:
        if y < min_y:
            min_y = y
        if x < min_x:
            min_x = x
            
    return sorted([(y-min_y, x-min_x) for y, x in shape])

def rotate(block):
    return normalize([(x, -y) for y, x in block])

def solution(game_board, table):
    answer = 0
    blanks = search_block(0, game_board)
    blocks = search_block(1, table)
    
    check = [False] * len(blocks)
    
    for blank in blanks:
        for i, block in enumerate(blocks):
            if check[i]:
                continue
                
            current = block
            
            for _ in range(4):
                if blank == current:
                    answer += len(current)
                    check[i] = True
                    break
                
                current = rotate(current)
            
            if check[i]:
                break

    
    return answer