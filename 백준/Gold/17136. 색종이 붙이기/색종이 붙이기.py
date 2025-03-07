class Main:
    def __init__(self):
        self.grid = [list(map(int, input().split())) for _ in range(10)]
        self.paper = [5] * 5
        self.answer = 26

    def is_valid(self, sy, sx, ey, ex):  # 주어진 영역 안에 하나의 색종이를 붙일 수 있는지 확인
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                if not self.grid[y][x]:
                    return False

        return True

    def do_action(self, sy, sx, ey, ex, state):
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                self.grid[y][x] = state

    def search(self, cnt=0):
        if self.answer <= cnt:  # 가지치기
            return
        for y in range(10):
            for x in range(10):
                if self.grid[y][x]:
                    for size in range(5):
                        my, mx = y + size, x + size
                        if self.paper[size] and my < 10 and mx < 10 and self.is_valid(y, x, my, mx):
                            self.do_action(y, x, my, mx, 0)
                            self.paper[size] -= 1
                            self.search(cnt + 1)
                            self.paper[size] += 1
                            self.do_action(y, x, my, mx, 1)

                    return  # 모든 색종이에 대해 확인을 끝냈다면 종료

        self.answer = min(self.answer, cnt)

    def solve(self):
        self.search()
        print(-1 if self.answer == 26 else self.answer)


problem = Main()
problem.solve()