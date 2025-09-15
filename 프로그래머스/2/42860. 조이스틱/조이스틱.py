def solution(name):
    vertical_moves = sum(min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1) for ch in name)

    move = len(name) - 1
    for i in range(len(name)):
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        move = min(move, i*2 + len(name) - next_idx)
        move = min(move, i + (len(name) - next_idx) * 2)

    return vertical_moves + move
