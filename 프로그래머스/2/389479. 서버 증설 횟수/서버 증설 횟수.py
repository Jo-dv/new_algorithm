def solution(players, m, k):
    answer = 0
    size = len(players)
    server = [0] * size
    answer = 0
    
    for i in range(size):
        if players[i] >= m:
            n = players[i] // m  # 현재 필요한 서버 수
            
            if server[i] < n:  # 서버 부족
                extra_server = n - server[i]
                if n * m <= players[i] < (n+1) * m:  # 증설했을 때 인원이 수용 가능하다면
                    answer += extra_server
                    for j in range(i, min(i+k, len(server))):
                        server[j] += extra_server
                    
    return answer