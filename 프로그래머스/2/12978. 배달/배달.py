import heapq

def solution(N, road, K):
    answer = 0
    
    graph = {i: [] for i in range(1, N+1)}
    for r in road:
        a, b, c = r
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    costs = [float("inf")] * (N+1)
    costs[1] = 0
    hq = [(0, 1)]
    
    while hq:
        cost, current = heapq.heappop(hq)
        
        if costs[current] < cost:
            continue
        
        for nxt_cost, nxt_node in graph[current]:
            if costs[current] + nxt_cost < costs[nxt_node]:
                costs[nxt_node] = costs[current] + nxt_cost
                heapq.heappush(hq, (costs[nxt_node], nxt_node))
        
    for i in range(1, N+1):
        if costs[i] <= K:
            answer += 1
            
    return answer