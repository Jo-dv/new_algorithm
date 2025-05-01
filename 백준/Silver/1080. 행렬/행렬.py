class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.a = [list(map(int, input())) for _ in range(self.n)]
        self.b = [list(map(int, input())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        for i in range(self.n - 2):
            for j in range(self.m - 2):
                if self.a[i][j] != self.b[i][j]:
                    for k in range(i, i + 3):
                        for l in range(j, j + 3):
                            self.a[k][l] = 1 - self.a[k][l]
                    self.answer += 1

        if self.a == self.b:
            print(self.answer)
        else:
            print(-1)


problem = Main()
problem.solve()
