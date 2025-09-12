def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time_str):
        m, s = map(int, time_str.split(":"))
        return m * 60 + s

    def to_mmss(seconds):
        m = seconds // 60
        s = seconds % 60
        return f"{m:02d}:{s:02d}"

    video_len_sec = to_seconds(video_len)
    pos_sec = to_seconds(pos)
    op_start_sec = to_seconds(op_start)
    op_end_sec = to_seconds(op_end)

    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    for c in commands:
        if c == "prev":
            pos_sec = max(pos_sec - 10, 0)
        elif c == "next":
            pos_sec = min(pos_sec + 10, video_len_sec)

        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return to_mmss(pos_sec)
