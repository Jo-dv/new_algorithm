def solution(plans):
    answer = []
    stack = []

    new_plans = []
    for name, start, playtime in plans:
        h, m = map(int, start.split(":"))
        new_plans.append([h*60 + m, name, int(playtime)])
    
    new_plans.sort()
    
    for i in range(len(new_plans)):
        start, name, time = new_plans[i]
        
        if i < len(new_plans) - 1:
            next_start = new_plans[i+1][0]
            remain = next_start - start
        else:
            remain = time
        
        if time <= remain:
            answer.append(name)
            remain -= time
            
            while remain > 0 and stack:
                prev_name, prev_time = stack.pop()
                if prev_time <= remain:
                    answer.append(prev_name)
                    remain -= prev_time
                else:
                    stack.append((prev_name, prev_time - remain))
                    break
        else:
            stack.append((name, time - remain))

    while stack:
        answer.append(stack.pop()[0])
    
    return answer