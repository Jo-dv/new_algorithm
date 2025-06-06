from collections import deque


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = 0

    def is_valid(self, y, x, visited):
        return 0 <= y < self.n and 0 <= x < self.n and not visited[y][x]

    def find_blocks(self):
        best = []
        visited = [[False] * self.n for _ in range(self.n)]

        for y in range(self.n):
            for x in range(self.n):
                if 1 <= self.grid[y][x]:
                    standard, total_cord, rainbow_cnt = self.grid[y][x], [(y, x)], 0
                    dq = deque([(y, x)])
                    visited[y][x] = True

                    while dq:
                        cy, cx = dq.popleft()

                        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            my, mx = cy + dy, cx + dx
                            if self.is_valid(my, mx, visited) and (self.grid[my][mx] == standard or self.grid[my][mx] == 0):
                                dq.append((my, mx))
                                visited[my][mx] = True
                                total_cord.append((my, mx))
                                if self.grid[my][mx] == 0:
                                    rainbow_cnt += 1

                    for cy, cx in total_cord:
                        if self.grid[cy][cx] == 0:
                            visited[cy][cx] = False

                    if len(total_cord) >= 2:
                        best.append((y, x, total_cord, rainbow_cnt))

        best.sort(key=lambda i: (-len(i[2]), -i[3], -i[0], -i[1]))
        return best[0] if best else []

    def remove_blocks(self, blocks):
        self.answer += len(blocks)**2

        for y, x in blocks:
            self.grid[y][x] = -10

    def down_blocks(self):
        for x in range(self.n):
            stack = []
            for y in range(self.n):
                if 0 <= self.grid[y][x]:
                    stack.append(self.grid[y][x])
                elif self.grid[y][x] == -1:
                    for i in range(y-1, -1, -1):
                        if self.grid[i][x] == -1:
                            break
                        if not stack:
                            self.grid[i][x] = -10
                        else:
                            self.grid[i][x] = stack.pop()
            if stack:
                for i in range(self.n-1, -1, -1):
                    if self.grid[i][x] == -1:
                        break
                    if not stack:
                        self.grid[i][x] = -10
                    else:
                        self.grid[i][x] = stack.pop()

    def rotate_blocks(self):
        new_grid = [i[:] for i in self.grid]
        for i in range(self.n):
            for j in range(self.n):
                new_grid[self.n-j-1][i] = self.grid[i][j]

        self.grid = new_grid

    def solve(self):
        while True:
            blocks = self.find_blocks()  # standard_y, standard_x, blocks_cord, rainbow_cnt
            if not blocks:
                break
            self.remove_blocks(blocks[2])
            self.down_blocks()
            self.rotate_blocks()
            self.down_blocks()

        print(self.answer)


problem = Main()
problem.solve()