import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.r, self.c = map(int, input().split())
        self.grid = [list(input()) for _ in range(self.r)]
        self.hr, self.hc = map(lambda i: int(i)-1, input().split())
        self.records = input()
        self.answer = [["#"] * self.c for _ in range(self.r)]
        self.visited = [[False] * self.c for _ in range(self.r)]

    def search(self, y, x):
        self.visited[y][x] = True
        dq = deque([(y, x)])
        check = self.grid[y][x]
        self.answer[y][x] = "."

        while dq:
            cy, cx = dq.popleft()

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                my, mx = cy + dy, cx + dx
                if 0 <= my < self.r and 0 <= mx < self.c and not self.visited[my][mx] and self.grid[my][mx] == check:
                    dq.append((my, mx))
                    self.visited[my][mx] = True
                    self.answer[my][mx] = "."

    def solve(self):
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

        for record in self.records:
            if record == "W":
                self.search(self.hr, self.hc)
            else:
                dy, dx = directions[record]
                self.hr += dy
                self.hc += dx

        self.answer[self.hr][self.hc] = "."
        for dy, dx in directions.values():
            my, mx = self.hr + dy, self.hc + dx
            if 0 <= my < self.r and 0 <= mx < self.c:
                self.answer[my][mx] = "."

        for i in self.answer:
            print("".join(i))


problem = Main()
problem.solve()
