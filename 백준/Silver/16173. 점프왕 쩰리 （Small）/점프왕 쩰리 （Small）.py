class Main:
    def __init__(self):
        self.n = int(input())
        self.grid = [list(map(int, input().split())) for _ in range(self.n)]
        self.visited = [[False] * self.n for _ in range(self.n)]

    def dfs(self, x, y):
        if x < 0 or y < 0 or x >= self.n or y >= self.n:
            return
        if self.visited[x][y]:
            return
        if self.grid[x][y] == -1:
            print("HaruHaru")
            exit()
        self.visited[x][y] = True
        jump = self.grid[x][y]
        if jump == 0:
            return
        self.dfs(x + jump, y)  # 아래로
        self.dfs(x, y + jump)  # 오른쪽으로

    def solve(self):
        self.dfs(0, 0)
        print("Hing")

problem = Main()
problem.solve()
