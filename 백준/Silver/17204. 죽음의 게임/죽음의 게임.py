class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.targets = [int(input()) for _ in range(self.n)]

    def solve(self):
        visited = [False] * self.n
        visited[0] = True
        current = 0
        call = 1

        while True:
            current = self.targets[current]
            if visited[current]:
                print(-1)
                return
            if current == self.k:
                print(call)
                return
            call += 1
            visited[current] = True


problem = Main()
problem.solve()
