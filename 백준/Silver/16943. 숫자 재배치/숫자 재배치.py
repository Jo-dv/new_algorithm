class Main:
    def __init__(self):
        self.a, self.b = input().split()
        self.check = set()
        self.answer = -1

    def search(self, num, visited):
        if len(num) == len(self.a):
            if num[0] == '0':
                return
            n = int(num)
            if n < int(self.b):
                self.answer = max(self.answer, n)
            return

        for i in range(len(self.a)):
            if visited[i]:
                continue

            if i > 0 and self.a[i] == self.a[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            self.search(num + self.a[i], visited)
            visited[i] = False

    def solve(self):
        if len(self.a) > len(self.b):
            print(-1)
            return

        self.a = sorted(self.a)
        visited = [False] * len(self.a)
        self.search('', visited)

        print(self.answer if self.answer != -1 else -1)


problem = Main()
problem.solve()
