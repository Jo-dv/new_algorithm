from collections import deque
from itertools import combinations as comb


class Main:
    def __init__(self):
        self.grid = [list(input()) for _ in range(5)]
        self.answer = 0

    def solve(self):
        cord = [(y, x) for y in range(5) for x in range(5)]

        for i in comb(cord, 7):
            s_cnt = sum(1 for y, x in i if self.grid[y][x] == "S")
            if s_cnt < 4:
                continue

            dq = deque([i[0]])
            visited = {i[0]}

            while dq:
                y, x = dq.popleft()
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    my, mx = y + dy, x + dx
                    if 0 <= my < 5 and 0 <= mx < 5 and (my, mx) not in visited and (my, mx) in i:
                        dq.append((my, mx))
                        visited.add((my, mx))

            if len(visited) == 7:
                self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()