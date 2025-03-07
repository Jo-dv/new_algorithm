class Main:
    def __init__(self):
        self.grid = [list(map(int, input().split())) for _ in range(10)]
        self.paper = [5] * 5
        self.answer = 26  # 최악의 경우 25개까지 사용 가능

    def is_valid(self, sy, sx, ey, ex):  # 해당 영역에 색종이를 붙일 수 있는지 확인
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                if not self.grid[y][x]:
                    return False
        return True

    def do_action(self, sy, sx, ey, ex, state):
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                self.grid[y][x] = state

    def next_position(self, y, x):  # (y, x) 이후 첫 번째 1의 위치 찾기
        for i in range(y, 10):
            for j in range(10):
                if i == y and j < x:  # 현재 줄에서는 x 이후부터 탐색
                    continue
                if self.grid[i][j]:
                    return i, j
        return -1, -1  # 더 이상 남은 1이 없으면 종료 조건

    def search(self, y=0, x=0, count=0):
        if count >= self.answer:  # 가지치기
            return

        ny, nx = self.next_position(y, x)
        if ny == -1:  # 더 이상 덮을 1이 없으면 최적해 갱신
            self.answer = min(self.answer, count)
            return

        for size in range(5):
            my, mx = ny + size, nx + size
            if self.paper[size] and my < 10 and mx < 10 and self.is_valid(ny, nx, my, mx):
                self.do_action(ny, nx, my, mx, 0)
                self.paper[size] -= 1
                self.search(ny, nx, count + 1)
                self.paper[size] += 1
                self.do_action(ny, nx, my, mx, 1)

    def solve(self):
        self.search()
        print(-1 if self.answer == 26 else self.answer)


problem = Main()
problem.solve()
