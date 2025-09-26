from itertools import combinations as cb

def solution(orders, course):
    answer = []

    for i in course:
        result = dict()
        for order in orders:
            order = "".join(sorted(list(order)))
            for data in cb(order, i):
                if data not in result:
                    result[data] = 1
                else:
                    result[data] += 1
        
        for k, v in result.items():
            if v >= 2 and v == max(result.values()):
                answer.append("".join(k))
    
    answer.sort()
    return answer