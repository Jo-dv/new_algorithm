class Main:
    def __init__(self):
        self.n, self.l = map(int, input().split())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = 0

    def search(self, line):
        visited = [False] * self.n

        for i in range(self.n - 1):
            if line[i] == line[i + 1]:
                continue
            elif line[i] + 1 == line[i + 1]:  # 오르막 직전
                for j in range(i, i - self.l, -1):  # 경사로를 오르막으로 위치시킨 후, 지나온 길들에 대해 조건 탐색
                    if j < 0 or line[j] != line[i] or visited[j]:
                        return False
                    visited[j] = True
            elif line[i] - 1 == line[i + 1]:  # 내리막 직전
                for j in range(i + 1, i + self.l + 1):  # 경사로를 내리막으로 위치시킨 후, 앞으로 이어진 길들에 대해 조건 탐색
                    if j >= self.n or line[j] != line[i + 1] or visited[j]:
                        return False
                    visited[j] = True
            else:  # 높이 차이가 2이상
                return False

        return True

    def solve(self):
        for row in self.grid:
            if self.search(row):
                self.answer += 1

        for col in zip(*self.grid):
            if self.search(col):
                self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()
