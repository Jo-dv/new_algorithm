def solution(storey):
    answer = 0
    
    while storey > 0:
        current = storey % 10
        nxt = (storey // 10) % 10
        
        if current < 5:
            answer += current
            storey //= 10
        elif current > 5:
            answer += (10 - current)
            storey = storey // 10 + 1
        else:
            if nxt >= 5:
                answer += (10 - current)
                storey = storey // 10 + 1
            else:
                answer += current
                storey //= 10
    
    return answer