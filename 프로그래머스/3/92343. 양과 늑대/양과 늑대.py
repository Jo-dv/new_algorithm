def solution(info, edges):
    global answer, graph
    answer = 0
    graph = {i: [] for i in range(len(info))}
    
    for edge in edges:
        p, c = edge
        graph[p].append(c)
    
    search(info, [0], 0, 0)
    return answer

def search(info, candidates, current_sheep, current_wolf): 
    global answer, graph
    
    for current in candidates:
        next_sheep = current_sheep
        next_wolf = current_wolf
        
        if info[current] == 0:
            next_sheep += 1
        else:
            next_wolf += 1
            
        if next_wolf >= next_sheep:
            continue
        
        answer = max(answer, next_sheep)
        next_candidates = [i for i in candidates if i != current]
        next_candidates.extend(graph[current])
        search(info, next_candidates, next_sheep, next_wolf)
        
            
        