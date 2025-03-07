import sys

class Main:
    def __init__(self):
        self.grid = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
        self.paper = [5] * 5  # 색종이 개수
        self.answer = 26

        # DP 배열 (dp[y][x]는 (y, x)를 좌상단으로 하는 최대 정사각형 크기)
        self.dp = [[0] * 10 for _ in range(10)]
        self.calculate_dp()

    def calculate_dp(self):
        """ DP 테이블을 채움 """
        for y in range(9, -1, -1):
            for x in range(9, -1, -1):
                if self.grid[y][x] == 1:
                    if y == 9 or x == 9:
                        self.dp[y][x] = 1  # 격자의 마지막 행/열은 그대로 1 유지
                    else:
                        self.dp[y][x] = min(self.dp[y+1][x], self.dp[y][x+1], self.dp[y+1][x+1]) + 1

    def is_valid(self, y, x, size):
        """ (y, x)에서 size x size 색종이를 붙일 수 있는지 확인 """
        if y + size > 10 or x + size > 10:  # 범위 초과
            return False
        for i in range(y, y + size):
            for j in range(x, x + size):
                if self.grid[i][j] == 0:
                    return False
        return True

    def do_action(self, y, x, size, state):
        """ (y, x)에서 size x size 영역을 state(0 or 1)로 변경 """
        for i in range(y, y + size):
            for j in range(x, x + size):
                self.grid[i][j] = state

    def search(self, y=0, x=0, cnt=0):
        """ 백트래킹으로 최소 개수 색종이 찾기 """
        if cnt >= self.answer:  # 현재 최소 개수보다 크면 중단 (가지치기)
            return

        # 다음 1을 찾음
        found = False
        for i in range(y, 10):
            for j in range(10):  # x는 항상 0부터 탐색
                if self.grid[i][j] == 1:
                    y, x = i, j
                    found = True
                    break
            if found:
                break

        if not found:  # 모든 1을 덮었다면 정답 갱신
            self.answer = min(self.answer, cnt)
            return

        # 최대 사용할 수 있는 색종이 크기 (최대 5x5)
        max_size = min(self.dp[y][x], 5)

        # 큰 색종이부터 시도
        for size in range(max_size, 0, -1):
            if self.paper[size-1] > 0 and self.is_valid(y, x, size):
                # 색종이 붙이기
                self.do_action(y, x, size, 0)
                self.paper[size-1] -= 1

                # 다음 탐색 (현재 위치 유지)
                self.search(y, x, cnt + 1)

                # 색종이 떼기 (백트래킹)
                self.do_action(y, x, size, 1)
                self.paper[size-1] += 1

    def solve(self):
        self.search()
        print(-1 if self.answer == 26 else self.answer)


if __name__ == "__main__":
    problem = Main()
    problem.solve()
