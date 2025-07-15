class Main:
    def __init__(self):
        self.n = int(input())
        self.arr = [int(input()) for _ in range(self.n)]

    def solve(self):
        answer = 0

        for i in range(self.n):
            cnt = 0
            for j in range(self.n):
                if self.arr[i] <= self.arr[j] <= self.arr[i] + 4:
                    cnt += 1

            answer = max(answer, cnt)

        print(5 - answer)


problem = Main()
problem.solve()