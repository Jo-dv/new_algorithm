from collections import deque


class Main:
    def __init__(self):
        self.n = int(input())
        self.t = int(input())
        self.apart = list(map(int, input().split()))
        self.call = list(map(int, input().split()))
        self.answer = []

    def solve(self):
        self.apart = deque(self.apart)
        for i in range(self.t):
            for _ in range(self.call[i] - 1):
                self.apart.append(self.apart.popleft())
            self.answer.append(self.apart[0])

        print(*self.answer)


problem = Main()
problem.solve()
