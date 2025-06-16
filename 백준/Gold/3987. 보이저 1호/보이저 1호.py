from collections import deque

class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.grid = [list(input()) for _ in range(self.n)]
        self.pr, self.pc = map(lambda i: int(i) - 1, input().split())
        self.answer = ""
        self.best_time = 0

        # 방향: U=0, R=1, D=2, L=3
        self.dirs = ['U', 'R', 'D', 'L']
        self.dy = [-1, 0, 1, 0]
        self.dx = [0, 1, 0, -1]
        self.reflect = {
            '/': [1, 0, 3, 2],
            '\\': [3, 2, 1, 0]
        }

    def solve(self):
        for i in range(4):  # 0:U, 1:R, 2:D, 3:L
            visited = [[[False]*4 for _ in range(self.m)] for _ in range(self.n)]
            y, x, d = self.pr, self.pc, i
            time = 0
            infinite_loop = False

            while True:
                if visited[y][x][d]:
                    infinite_loop = True
                    break
                visited[y][x][d] = True

                ny = y + self.dy[d]
                nx = x + self.dx[d]
                time += 1

                if ny < 0 or ny >= self.n or nx < 0 or nx >= self.m:
                    break
                if self.grid[ny][nx] == 'C':
                    break

                cell = self.grid[ny][nx]
                if cell in self.reflect:
                    d = self.reflect[cell][d]

                y, x = ny, nx

            if infinite_loop:
                print(self.dirs[i])
                print("Voyager")
                return
            elif time > self.best_time:
                self.answer = self.dirs[i]
                self.best_time = time

        print(self.answer)
        print(self.best_time)


problem = Main()
problem.solve()
