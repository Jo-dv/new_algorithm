def solution(picks, minerals):
    answer = 0
    total_picker = sum(picks) * 5
    minerals = minerals[:total_picker]
    results = []
    
    for i in range(0, len(minerals), 5):
        group = minerals[i:i+5]
        counter = {"diamond": 0, "iron": 0, "stone": 0}
        for k in group:
            counter[k] += 1
        results.append([counter["diamond"], counter["iron"], counter["stone"]])
    results.sort(key=lambda item: (-item[0], -item[1], -item[2]))
    
    for dia, iron, stone in results:
        if picks[0] > 0:
            picks[0] -= 1
            answer += (dia * 1) + (iron * 1) + (stone * 1)
        elif picks[1] > 0:
            picks[1] -= 1
            answer += (dia * 5) + (iron * 1) + (stone * 1)
        elif picks[2] > 0:
            picks[2] -= 1
            answer += (dia * 25) + (iron * 5) + (stone * 1)
    
    return answer