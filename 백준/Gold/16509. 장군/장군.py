from collections import deque

class Main:
    def __init__(self):
        self.elephant = list(map(int, input().split()))
        self.king = list(map(int, input().split()))

    def solve(self):
        directions = {(-1, 0): [(-1, -1), (-1, 1)],
                      (1, 0): [(1, -1), (1, 1)],
                      (0, -1): [(-1, -1), (1, -1)],
                      (0, 1): [(-1, 1), (1, 1)]
                      }
        visited = [[False] * 9 for _ in range(10)]
        ey, ex = self.elephant
        visited[ey][ex] = True
        dq = deque([(ey, ex, 0)])

        while dq:
            cy, cx, step = dq.popleft()
            if [cy, cx] == self.king:
                print(step)
                return

            for forward in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                sy, sx = cy + forward[0], cx + forward[1]
                if (sy < 0 or sy >= 10 or sx < 0 or sx >= 9) or [sy, sx] == self.king:
                    continue

                for dy, dx in directions[forward]:
                    flag = True
                    ty, tx = sy, sx
                    for i in range(2):
                        ty += dy
                        tx += dx
                        if ty < 0 or ty >= 10 or tx < 0 or tx >= 9 or (i == 0 and [ty, tx] == self.king):
                            flag = False
                    if flag and not visited[ty][tx]:
                        dq.append((ty, tx, step + 1))
                        visited[ty][tx] = True

        print(-1)


problem = Main()
problem.solve()
