import sys
sys.setrecursionlimit(10**6)

def solution(n, m, x, y, r, c, k):
    x -= 1
    y -= 1
    r -= 1
    c -= 1

    answer = None

    directions = [
        ("d", 1, 0),
        ("l", 0, -1),
        ("r", 0, 1),
        ("u", -1, 0)
    ]

    def search(cx, cy, ck, result):
        nonlocal answer

        if answer is not None:
            return

        dist = abs(cx - r) + abs(cy - c)
        if dist > ck or (ck - dist) % 2 != 0:
            return

        if ck == 0:
            if cx == r and cy == c:
                answer = result
            return

        for key, dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < m:
                search(nx, ny, ck - 1, result + key)

    search(x, y, k, "")

    return answer if answer is not None else "impossible"
