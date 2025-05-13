from collections import deque
import sys
input = lambda: sys.stdin.readline()


class Main:
    def __init__(self):
        self.tc = int(input())
        self.w = self.h = None
        self.grid = None
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def find_start(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == "@":
                    return y, x

    def is_valid(self, y, x):
        return 0 <= y < self.h and 0 <= x < self.w

    def expand_fire(self):
        dq = deque([])
        fire_time = [[0] * self.w for _ in range(self.h)]
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == "*":
                    dq.append((y, x))
                    fire_time[y][x] = 1

        while dq:
            y, x = dq.popleft()
            for dy, dx in self.directions:
                my, mx = y + dy, x + dx
                if self.is_valid(my, mx) and self.grid[my][mx] == "." and fire_time[my][mx] == 0:
                    fire_time[my][mx] = fire_time[y][x] + 1
                    dq.append((my, mx))

        return fire_time

    def search(self, init_y, init_x, fire_time):
        dq = deque([(1, init_y, init_x)])
        visited = [[False] * self.w for _ in range(self.h)]
        visited[init_y][init_x] = True

        while dq:
            time, y, x = dq.popleft()
            if y == 0 or y == self.h - 1 or x == 0 or x == self.w - 1:
                return time

            for dy, dx in self.directions:
                my, mx = y + dy, x + dx
                if self.is_valid(my, mx) and not visited[my][mx] and self.grid[my][mx] == ".":
                    if time + 1 < fire_time[my][mx] or fire_time[my][mx] == 0:
                        dq.append((time + 1, my, mx))
                        visited[my][mx] = True

        return "IMPOSSIBLE"

    def solve(self):
        answers = []

        for _ in range(self.tc):
            self.w, self.h = map(int, input().split())
            self.grid = [list(input()) for _ in range(self.h)]
            y, x = self.find_start()
            fire_time = self.expand_fire()
            answer = self.search(y, x, fire_time)
            answers.append(str(answer))

        print("\n".join(answers))


problem = Main()
problem.solve()