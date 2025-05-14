from collections import deque


class Main:
    def __init__(self):
        self.n, self.m, self.p = map(int, input().split())
        self.s = [0] + list(map(int, input().split()))
        self.grid = [list(input().strip()) for _ in range(self.n)]
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.q = [deque() for _ in range(self.p + 1)]
        self.answer = [0] * (self.p + 1)

        for y in range(self.n):
            for x in range(self.m):
                if self.grid[y][x].isdigit():
                    player = int(self.grid[y][x])
                    self.q[player].append((y, x))
                    self.answer[player] += 1

    def solve(self):
        while True:
            any_expansion = False
            for player in range(1, self.p + 1):
                s = self.s[player]
                step = 0
                curr_q = self.q[player]

                # 단계별 큐 확장
                while curr_q and step < s:
                    next_q = deque()
                    while curr_q:
                        y, x = curr_q.popleft()
                        for dy, dx in self.dirs:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < self.n and 0 <= nx < self.m and self.grid[ny][nx] == '.':
                                self.grid[ny][nx] = str(player)
                                self.answer[player] += 1
                                next_q.append((ny, nx))
                                any_expansion = True
                    curr_q = next_q
                    step += 1
                # 다음 턴을 위해 갱신
                self.q[player] = curr_q

            if not any_expansion:
                break

        print(*self.answer[1:])


problem = Main()
problem.solve()
