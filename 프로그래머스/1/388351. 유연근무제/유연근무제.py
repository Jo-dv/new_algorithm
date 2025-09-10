def solution(schedules, timelogs, startday):
    answer = 0
    
    for i, schedule in enumerate(schedules):
        day = startday
        flag = False
        hour, minute = schedule // 100, schedule % 100 + 10
        if minute > 59:
            hour += 1
            minute = minute % 60
        standard = hour * 100 + minute
        for timelog in timelogs[i]:
            if day not in [6, 7] and timelog > standard:
                flag = True
                break
            day = (day % 7) + 1
        if not flag:
            answer += 1
    return answer