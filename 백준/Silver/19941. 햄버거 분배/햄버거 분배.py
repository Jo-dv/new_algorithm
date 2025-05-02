class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.table = list(input())
        self.answer = 0

    def solve(self):
        for i in range(self.n):
            if self.table[i] == 'P':
                start = max(0, i - self.k)
                end = min(self.n - 1, i + self.k)
                for j in range(start, end + 1):
                    if self.table[j] == 'H':
                        self.table[j] = 'X'  # 먹힌 햄버거는 표시
                        self.answer += 1
                        break

        print(self.answer)


problem = Main()
problem.solve()
