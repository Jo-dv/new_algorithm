def min_to_sec(start, end):
    start = start.split(":")
    end = end.split(":")
    
    return (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))

def change_code(code):
    new_code = ""
    i = 0
    while i < len(code):
        if i+1 < len(code) and code[i+1] == "#":
            if code[i] == "C":
                new_code += "V"
            elif code[i] == "D":
                new_code += "W"
            elif code[i] == "F":
                new_code += "X"
            elif code[i] == "G":
                new_code += "Y"
            elif code[i] == "A":
                new_code += "Z"
            i += 2
        else:
            new_code += code[i]
            i += 1
    
    return new_code
    

def solution(m, musicinfos):
    answer = ["", 0]
    m = change_code(m)
    
    for i in musicinfos:
        s, e, t, c = i.split(",")
        c = change_code(c)
        time_slice = min_to_sec(s, e)
        if time_slice < len(c):
            c = c[:time_slice]
        elif time_slice > len(c):
            c = c * (time_slice // len(c)) + c[:(time_slice % len(c))]
    
        if m in c:
            if answer[1] < time_slice:
                answer = [t, time_slice]
            
    if answer[0] == "":
        return "(None)"
    
    return answer[0]