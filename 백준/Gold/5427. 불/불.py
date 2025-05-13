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
        fire_info = [[0] * self.w for _ in range(self.h)]
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == "*":
                    dq.append((y, x))
                    fire_info[y][x] = 1

        while dq:
            y, x = dq.popleft()
            for dy, dx in self.directions:
                my, mx = y + dy, x + dx
                if self.is_valid(my, mx) and self.grid[my][mx] == "." and fire_info[my][mx] == 0:
                    fire_info[my][mx] = fire_info[y][x] + 1
                    dq.append((my, mx))

        return fire_info

    def search(self, init_y, init_x, fire_info):
        dq = deque([(1, init_y, init_x)])
        visited = [[False] * self.w for _ in range(self.h)]
        visited[init_y][init_x] = True

        while dq:
            time, y, x = dq.popleft()
            if y == 0 or y == self.h - 1 or x == 0 or x == self.w - 1:
                print(time)
                return

            for dy, dx in self.directions:
                my, mx = y + dy, x + dx
                if self.is_valid(my, mx) and not visited[my][mx] and self.grid[my][mx] == "." and (time + 1 < fire_info[my][mx] or fire_info[my][mx] == 0):
                    dq.append((time + 1, my, mx))
                    visited[my][mx] = True

        print("IMPOSSIBLE")
        return

    def solve(self):
        for _ in range(self.tc):
            self.w, self.h = map(int, input().split())
            self.grid = [list(input()) for _ in range(self.h)]
            y, x = self.find_start()
            fire_info = self.expand_fire()
            self.search(y, x, fire_info)


problem = Main()
problem.solve()